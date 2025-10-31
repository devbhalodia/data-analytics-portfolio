import os
import pandas as pd
from sqlalchemy import create_engine
import json

METADATA_PATH = "etl/metadata.json"

def ensure_dirs(*dirs):
    for d in dirs:
        if d and not os.path.exists(d):
            os.makedirs(d, exist_ok=True)

def load_metadata():
    if os.path.exists(METADATA_PATH):
        with open(METADATA_PATH, "r") as f:
            return json.load(f)
    else:
        return {"last_stock_date": None, "last_news_date": None}

def save_metadata(meta):
    ensure_dirs(os.path.dirname(METADATA_PATH) or ".")
    with open(METADATA_PATH, "w") as f:
        json.dump(meta, f, indent=4)
    print(f"[INFO] Metadata updated: {meta}")

def to_date_str(dt):
    if pd.isna(dt) or dt is None:
        return None
    return pd.to_datetime(dt).strftime("%Y-%m-%d")

def max_date(d1, d2):
    if not d1: return d2
    if not d2: return d1
    return d1 if d1 >= d2 else d2

def load_to_mysql(stocks_path, news_path, db_url=None):
    if db_url is None:
        db_url = 'mysql+pymysql://root:Rudraksh902.@127.0.0.1:3306/market'

    engine = create_engine(db_url)

    # --- Load metadata ---
    meta = load_metadata()
    last_stock = pd.to_datetime(meta.get("last_stock_date")) if meta.get("last_stock_date") else None
    last_news = pd.to_datetime(meta.get("last_news_date")) if meta.get("last_news_date") else None

    # --- Read processed data ---
    df_stocks_all = pd.read_parquet(stocks_path)
    df_stocks_all["date"] = pd.to_datetime(df_stocks_all["date"], errors="coerce")

    df_news_all = pd.read_parquet(news_path)
    df_news_all["date"] = pd.to_datetime(df_news_all["date"], errors="coerce")

    # --- Filter for incremental load ---
    df_stocks_new = df_stocks_all if last_stock is None else df_stocks_all[df_stocks_all["date"] > last_stock]
    df_news_new   = df_news_all   if last_news  is None else df_news_all[df_news_all["date"] > last_news]

    df_stocks_new = df_stocks_new.dropna(subset=["date", "ticker"])
    df_news_new   = df_news_new.dropna(subset=["date", "ticker"])

    df_stocks_new["date"] = df_stocks_new["date"].dt.strftime("%Y-%m-%d")
    df_news_new["date"]   = df_news_new["date"].dt.strftime("%Y-%m-%d")

    # --- Load new data ---
    if not df_stocks_new.empty:
        df_stocks_new.to_sql("stocks", con=engine, if_exists="append", index=False)
        print(f"[INFO] Loaded {len(df_stocks_new)} new stock rows.")
    else:
        print("[INFO] No new stock rows to load.")

    if not df_news_new.empty:
        df_news_new.to_sql("news", con=engine, if_exists="append", index=False)
        print(f"[INFO] Loaded {len(df_news_new)} new news rows.")
    else:
        print("[INFO] No new news rows to load.")

    # --- Update metadata ---
    latest_stock_date = df_stocks_all["date"].max() if not df_stocks_all.empty else None
    latest_news_date  = df_news_all["date"].max()  if not df_news_all.empty else None

    new_meta = {
        "last_stock_date": to_date_str(max_date(to_date_str(meta.get("last_stock_date")), to_date_str(latest_stock_date))),
        "last_news_date":  to_date_str(max_date(to_date_str(meta.get("last_news_date")), to_date_str(latest_news_date)))
    }

    save_metadata(new_meta)

def main():
    processed_dir = "data/processed"
    stocks_path = os.path.join(processed_dir, "stocks_clean.parquet")
    news_path = os.path.join(processed_dir, "news_clean.parquet")

    if not os.path.exists(stocks_path):
        raise FileNotFoundError(f"Stocks file not found: {stocks_path}")
    if not os.path.exists(news_path):
        raise FileNotFoundError(f"News file not found: {news_path}")

    load_to_mysql(stocks_path, news_path)

if __name__ == "__main__":
    main()
