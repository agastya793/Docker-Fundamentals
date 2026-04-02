import pandas as pd

def create_features(df):
    df = df.copy()
    df["date"] = pd.to_datetime(df["date"])

    df["day_of_week"] = df["date"].dt.dayofweek
    df["month"] = df["date"].dt.month
    df["day"] = df["date"].dt.day
    df["is_weekend"] = df["day_of_week"].isin([5, 6]).astype(int)

    df["sales_lag_1"] = df["sales"].shift(1)
    df["sales_lag_7"] = df["sales"].shift(7)
    df["rolling_mean_7"] = df["sales"].shift(1).rolling(window=7).mean()

    return df