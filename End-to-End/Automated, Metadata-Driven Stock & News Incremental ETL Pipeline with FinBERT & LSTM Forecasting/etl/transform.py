import os
import yaml
import json
import torch
import numpy as np
import pandas as pd
from pathlib import Path
from transformers import AutoTokenizer, AutoModelForSequenceClassification

METADATA_PATH = "etl/metadata.json"

# -----------------------------
# Utility Functions
# -----------------------------
def makenan(value):
    try:
        return np.nan if value < 0 else value
    except Exception:
        return np.nan

def load_config(path="etl/config.yaml"):
    with open(path, "r") as f:
        cfg = yaml.safe_load(f)
    for k, v in cfg.items():
        if isinstance(v, str) and v.startswith("<ENV:") and v.endswith(">"):
            env_key = v[5:-1]
            cfg[k] = os.environ.get(env_key)
    return cfg

def ensure_dirs(*dirs):
    for d in dirs:
        Path(d).mkdir(parents=True, exist_ok=True)

def load_metadata():
    if os.path.exists(METADATA_PATH):
        with open(METADATA_PATH, "r") as f:
            return json.load(f)
    ensure_dirs(os.path.dirname(METADATA_PATH) or ".")
    meta = {"last_stock_date": None, "last_news_date": None}
    with open(METADATA_PATH, "w") as f:
        json.dump(meta, f, indent=4)
    return meta

# -----------------------------
# STOCK TRANSFORM
# -----------------------------
def transform_stocks(input_path, output_path, last_stock_date=None):

    df_stocks = pd.read_csv(input_path)
    stock_first_row = df_stocks.iloc[0:1, :]
    ticker_list = []

    for i in stock_first_row.iloc[0]:
        if pd.notna(i) and i not in ticker_list:
            ticker_list.append(i)

    all_tickers = []

    for i in range(len(ticker_list)):
        suffix = ''
        if i != 0:
            suffix = '.' + str(i)

        cols = ["date", "open" + suffix, "high" + suffix, "low" + suffix, "close" + suffix, "volume" + suffix]
        missing = [c for c in cols if c not in df_stocks.columns]
        if missing:
            print(f"[WARN] Skipping {ticker_list[i]} (missing {missing})")
            continue

        temp = df_stocks[cols].copy()
        temp.columns = ["date", "open", "high", "low", "close", "volume"]
        temp.dropna(inplace=True)

        temp["ticker"] = ticker_list[i]
        temp.drop_duplicates(subset=["date", "ticker"], inplace=True)

        num_cols = ["open", "high", "low", "close", "volume"]
        for col in num_cols:
            temp[col] = pd.to_numeric(temp[col], errors="coerce")

        temp["date"] = pd.to_datetime(temp["date"], errors="coerce")

        # Apply makenan (assuming defined earlier)
        for col in num_cols:
            temp[col] = temp[col].apply(makenan)

        temp["ticker"] = temp["ticker"].str.strip().str.lower()

        # Derived metrics
        temp["daily_pct_change"] = (temp["close"] - temp["open"]) / temp["open"] * 100
        temp["price_range"] = temp["high"] - temp["low"]
        temp["daily_return"] = temp["close"].pct_change() * 100
        temp["cumulative_return"] = ((1 + temp["daily_return"] / 100).cumprod() - 1) * 100

        # --- Incremental filtering ---
        if last_stock_date is not None:
            temp = temp[temp["date"] > pd.to_datetime(last_stock_date)]

        all_tickers.append(temp)

    if not all_tickers:
        print("[WARN] No valid tickers to process.")
        return

    df_stocks = pd.concat(all_tickers, ignore_index=True)

    # Save clean data
    if not all_tickers:
        print("[WARN] No valid tickers to process.")
        return

    df_stocks = pd.concat(all_tickers, ignore_index=True)

    # --- Combine with existing data (for true incremental append) ---
    if os.path.exists(output_path):
        existing = pd.read_parquet(output_path)
        before_merge = len(existing)
        df_stocks = pd.concat([existing, df_stocks], ignore_index=True)
        df_stocks.drop_duplicates(subset=["date", "ticker"], inplace=True)
        after_merge = len(df_stocks)
        print(f"[INFO] Existing rows: {before_merge}")
        print(f"[INFO] Total after merge (deduped): {after_merge}")
        print(f"[INFO] Incremental rows added: {after_merge - before_merge}")

    # --- Save clean data ---
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df_stocks.to_parquet(output_path, index=False)

    print(f"[SUCCESS] Stocks transformed and saved → {output_path}")
    print(f"[INFO] Final rows: {len(df_stocks)} | Columns: {list(df_stocks.columns)}")

# -----------------------------
# SENTIMENT MODEL (FinBERT)
# -----------------------------
tokenizer = AutoTokenizer.from_pretrained("yiyanghkust/finbert-tone")
model = AutoModelForSequenceClassification.from_pretrained("yiyanghkust/finbert-tone")

def get_finbert_sentiment(text):
    if not isinstance(text, str) or not text.strip():
        return pd.Series([None, None])
    try:
        inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
        with torch.no_grad():
            outputs = model(**inputs)
        scores = torch.nn.functional.softmax(outputs.logits, dim=-1)
        labels = ["negative", "neutral", "positive"]
        predicted_label = labels[torch.argmax(scores)]
        sentiment_score = scores[0, torch.argmax(scores)].item()
        return pd.Series([predicted_label, sentiment_score])
    except Exception:
        return pd.Series([None, None])

# -----------------------------
# NEWS TRANSFORM
# -----------------------------
def transform_news(input_path, output_path, last_date=None):
    print("[INFO] Starting news transformation...")

    df_news = pd.read_csv(input_path)
    if df_news.empty:
        print("[WARN] Empty news CSV. Skipping.")
        return

    df_news["date"] = pd.to_datetime(df_news["date"], errors="coerce")
    df_news.dropna(subset=["date"], inplace=True)

    # Incremental filter
    if last_date:
        df_news = df_news[df_news["date"] > pd.to_datetime(last_date)]

    if df_news.empty:
        print("[INFO] No new news rows to transform.")
        return

    df_news.drop_duplicates(subset=["ticker", "date", "headline"], inplace=True)
    for col in ["ticker", "source"]:
        if col in df_news.columns:
            df_news[col] = df_news[col].astype(str).str.strip().str.lower()

    # Apply FinBERT
    sentiments = df_news["headline"].apply(get_finbert_sentiment)
    sentiments.columns = ["sentiment_label", "sentiment_score"]
    df_news = pd.concat([df_news.reset_index(drop=True), sentiments.reset_index(drop=True)], axis=1)

    # Combine with existing parquet if exists
    if os.path.exists(output_path):
        df_existing = pd.read_parquet(output_path)
        df_final = pd.concat([df_existing, df_news], ignore_index=True)
        df_final.drop_duplicates(subset=["ticker", "date", "headline"], inplace=True)
    else:
        df_final = df_news

    ensure_dirs(os.path.dirname(output_path))
    df_final.to_parquet(output_path, index=False)

    print(f"[INFO] News transformed and saved ({len(df_news)} new rows).")

# -----------------------------
# MAIN EXECUTION
# -----------------------------
def main():
    cfg = load_config()
    raw_dir = cfg.get("raw_dir", "data/raw")
    processed_dir = cfg.get("processed_dir", "data/processed")
    metadata = load_metadata()

    input_path_stocks = os.path.join(raw_dir, "stocks.csv")
    output_path_stocks = os.path.join(processed_dir, "stocks_clean.parquet")
    input_path_news = os.path.join(raw_dir, "news.csv")
    output_path_news = os.path.join(processed_dir, "news_clean.parquet")

    if not os.path.exists(input_path_stocks):
        raise FileNotFoundError(f"Input file not found: {input_path_stocks}")
    if not os.path.exists(input_path_news):
        raise FileNotFoundError(f"Input file not found: {input_path_news}")

    transform_stocks(input_path_stocks, output_path_stocks, metadata.get("last_stock_date"))
    transform_news(input_path_news, output_path_news, metadata.get("last_news_date"))

    print("[SUCCESS] Transform stage completed successfully.")

if __name__ == "__main__":
    main()
