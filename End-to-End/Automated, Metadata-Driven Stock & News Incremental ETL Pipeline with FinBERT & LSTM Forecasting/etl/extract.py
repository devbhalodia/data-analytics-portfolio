import os, sys, yaml, time, requests, json
from datetime import datetime, timedelta
from pathlib import Path
import pandas as pd
import yfinance as yf
from dotenv import load_dotenv

load_dotenv()

DEFAULT_CONFIG = "etl/config.yaml"
DEFAULT_DAYS = 365
METADATA_PATH = "etl/metadata.json"

def load_config(path=DEFAULT_CONFIG):
    with open(path, "r") as f:
        cfg = yaml.safe_load(f)
    for k, v in cfg.items():
        if isinstance(v, str) and v.startswith("<ENV:") and v.endswith(">"):
            env_key = v[5:-1]
            cfg[k] = os.environ.get(env_key)
    return cfg

def ensure_dirs(*dirs):
    for d in dirs: Path(d).mkdir(parents=True, exist_ok=True)

def load_metadata():
    if os.path.exists(METADATA_PATH):
        with open(METADATA_PATH, "r") as f:
            return json.load(f)
    return {"last_stock_date": None, "last_news_date": None}

def get_stock_data(tickers, start_date, end_date):
    frames = []
    for t in tickers:
        df = yf.download(
            t,
            start=start_date,
            end=(end_date + timedelta(days=1)).isoformat(),
            interval="1d",
            progress=False
        )
        if not df.empty:
            df = df.reset_index()
            df["ticker"] = t
            df = df.rename(columns={
                "Date":"date","Open":"open","High":"high","Low":"low","Close":"close","Volume":"volume"
            })
            frames.append(df[["ticker","date","open","high","low","close","volume"]])
        time.sleep(0.2)
    return pd.concat(frames, ignore_index=True) if frames else pd.DataFrame()

def get_news_for_ticker(news_api_key, ticker, from_date, to_date):
    base = "https://newsapi.org/v2/everything"
    params = {
        "q": ticker, "language":"en","sortBy":"publishedAt",
        "from": from_date, "to": to_date, "pageSize":100,
        "apiKey": news_api_key
    }
    r = requests.get(base, params=params, timeout=30)
    if r.status_code != 200:
        print(f"[WARN] NewsAPI {r.status_code} for {ticker}")
        return pd.DataFrame(columns=["ticker","date","headline","source"])
    data = r.json().get("articles", [])
    rows = []
    for a in data:
        rows.append({
            "ticker": ticker,
            "date": a.get("publishedAt","")[:10],
            "headline": a.get("title",""),
            "source": (a.get("source") or {}).get("name","")
        })
    return pd.DataFrame(rows)

def main():
    cfg = load_config()
    tickers = cfg["tickers"]
    news_api_key = cfg["news_api_key"]
    raw_dir = cfg.get("raw_dir", "data/raw")
    ensure_dirs(raw_dir)

    metadata = load_metadata()  # read-only here; load will update master metadata after success
    today = datetime.utcnow().date()

    # === STOCK EXTRACTION ===
    if metadata.get("last_stock_date"):
        start_stock = datetime.strptime(metadata["last_stock_date"], "%Y-%m-%d").date() + timedelta(days=1)
        print(f"[INFO] Incremental stock extraction from {start_stock} to {today}")
    else:
        start_stock = today - timedelta(days=DEFAULT_DAYS)
        print(f"[INFO] First-time full stock extraction: {start_stock} to {today}")

    stocks = get_stock_data(tickers, start_stock.isoformat(), today)
    if not stocks.empty:
        ensure_dirs(raw_dir)
        stocks.to_csv(f"{raw_dir}/stocks.csv", index=False)
        print(f"Stocks saved ({len(stocks)} rows) to {raw_dir}/stocks.csv")
    else:
        print("[INFO] No new stock data available.")

    # === NEWS EXTRACTION ===
    if metadata.get("last_news_date"):
        start_news = datetime.strptime(metadata["last_news_date"], "%Y-%m-%d").date() + timedelta(days=1)
        print(f"[INFO] Incremental news extraction from {start_news} to {today}")
    else:
        start_news = today - timedelta(days=30)
        print(f"[INFO] First-time full news extraction: {start_news} to {today}")

    news_frames = []
    for t in tickers:
        df = get_news_for_ticker(news_api_key, t, start_news.isoformat(), today.isoformat())
        if not df.empty:
            news_frames.append(df)
        time.sleep(1)
    news = pd.concat(news_frames, ignore_index=True) if news_frames else pd.DataFrame()
    if not news.empty:
        ensure_dirs(raw_dir)
        news.to_csv(f"{raw_dir}/news.csv", index=False)
        print(f"News saved ({len(news)} rows) to {raw_dir}/news.csv")
    else:
        print("[INFO] No new news articles found.")

    # === IMPORTANT: do NOT update master metadata here. Load will update it after successful load. ===
    print("[INFO] Extraction complete. Raw CSVs written to data/raw/. Master metadata unchanged here.")

if __name__ == "__main__":
    main()
