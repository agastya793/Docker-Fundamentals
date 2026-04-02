import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor
from utils import create_features

# Load dataset
df = pd.read_csv("sample_data.csv")

# Feature engineering
df = create_features(df)
df = df.dropna()

# Features and target
features = [
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

X = df[features]
y = df["sales"]

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# Save model
joblib.dump(model, "model.pkl")

print("Model trained successfully and saved as model.pkl")