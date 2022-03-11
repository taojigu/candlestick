import pandas as pd


def fetch_data():
    df = pd.read_csv("time_price.csv")

    return df


def fetch_minute5_data():
    df = fetch_data()
    df["time"] = pd.to_datetime(df["time"])
    df["open"] = df["price"]
    df["close"] = df["price"]
    df["high"] = df["price"]
    df["low"] = df["price"]
    period_type = "5Min"
    minutes5 = df.resample(period_type, on="time").agg(
        {"open": "first", "close": "last", "high": "max", "low": "min"}).dropna()
    return minutes5
