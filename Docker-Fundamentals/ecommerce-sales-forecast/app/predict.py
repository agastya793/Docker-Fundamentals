import joblib
import pandas as pd

model = joblib.load("model.pkl")

FEATURES = [
    "orders",
    "ad_spend",
    "discount",
    "holiday",
    "day_of_week",
    "month",
    "day",
    "is_weekend",
    "sales_lag_1",
    "sales_lag_7",
    "rolling_mean_7"
]

def predict_sales(data: dict):
    df = pd.DataFrame([data])
    prediction = model.predict(df[FEATURES])[0]
    return round(float(prediction), 2)