from fastapi import FastAPI
from pydantic import BaseModel
from predict import predict_sales

app = FastAPI(title="eCommerce Sales Forecast API")

class SalesInput(BaseModel):
    orders: int
    ad_spend: float
    discount: float
    holiday: int
    day_of_week: int
    month: int
    day: int
    is_weekend: int
    sales_lag_1: float
    sales_lag_7: float
    rolling_mean_7: float

@app.get("/")
def home():
    return {"message": "eCommerce Sales Forecast API is running"}

@app.post("/predict")
def predict(input_data: SalesInput):
    prediction = predict_sales(input_data.dict())
    return {"predicted_sales": prediction}