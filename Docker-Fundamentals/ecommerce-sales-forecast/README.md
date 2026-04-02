# 📈 ECommerce Sales Forecasting API (Dockerized)

A machine learning-powered **ECommerce Sales Forecasting API** built using **Python, FastAPI, Scikit-learn, and Docker**.

This project predicts future eCommerce sales based on business-related input features such as:

- Orders
- Ad Spend
- Discount
- Holiday Indicator
- Historical Sales Trends

The application is fully **containerized using Docker**, managed with **Docker Compose**, and published to **Docker Hub** for easy sharing and deployment.

---

## 🚀 Project Highlights

- 📊 Sales forecasting using Machine Learning
- ⚡ FastAPI backend for prediction API
- 🧠 Feature engineering with lag and rolling statistics
- 🐳 Dockerized for consistent deployment
- 🌐 Docker Hub image published


---

## 🛠️ Tech Stack

- **Python**
- **Pandas**
- **Scikit-learn**
- **FastAPI**
- **Uvicorn**
- **Joblib**
- **Docker**
- **Docker Compose**

---

## 📂 Project Structure

```bash
ecommerce-sales-forecast/
│
├── app/
│   ├── main.py
│   ├── train.py
│   ├── predict.py
│   ├── utils.py
│   ├── sample_data.csv
│   └── model.pkl
│
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── .gitignore
└── README.md
```

---

## 📌 Problem Statement

Forecasting eCommerce sales is useful for:

- Inventory planning
- Marketing optimization
- Revenue forecasting
- Business decision-making

This project simulates a real-world ML deployment pipeline where a trained forecasting model is exposed through an API and deployed using Docker.

---

## 📊 Dataset

The project uses a sample Dummy (synthetic) eCommerce sales dataset 


### Example:

```csv
date,sales,orders,ad_spend,discount,holiday
2025-01-01,1200,45,300,10,1
2025-01-02,1100,40,250,5,0
2025-01-03,1400,50,320,15,0
```

---


## 🧠 Machine Learning Workflow

### 1. Data Loading
The dataset is loaded using **Pandas**.

### 2. Feature Engineering
Date-based and lag-based features are created.

### 3. Model Training
A **RandomForestRegressor** model is trained on historical data.

### 4. Model Serialization
The trained model is saved as:

```bash
model.pkl
```

### 5. API Inference
The model is loaded into a **FastAPI** application to serve predictions via an HTTP endpoint.

---

## 🔥 API Endpoints

### `GET /`
Health check endpoint.

#### Response:
```json
{
  "message": "eCommerce Sales Forecast API is running"
}
```

---

### `POST /predict`
Predicts eCommerce sales based on input features.

#### Sample Request:
```json
{
  "orders": 60,
  "ad_spend": 450,
  "discount": 20,
  "holiday": 0,
  "day_of_week": 2,
  "month": 3,
  "day": 28,
  "is_weekend": 0,
  "sales_lag_1": 1700,
  "sales_lag_7": 1550,
  "rolling_mean_7": 1650
}
```

#### Sample Response:
```json
{
  "predicted_sales": 1765.42
}
```



---

## 📄 Swagger API Documentation

After running the project locally or in Docker, open:

```bash
http://localhost:8000/docs
```

This provides an interactive interface to test the API.

---

# 🧪 Local Development Setup

## 1️⃣ Clone the repository

```bash
git clone this repo
cd ecommerce-sales-forecast
```

---

## 2️⃣ Create and activate virtual environment

### Windows PowerShell
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### Windows CMD
```cmd
python -m venv venv
venv\Scripts\activate
```

---

## 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Train the model

```bash
cd app
python train.py
```

This creates:

```bash
model.pkl
```

---

## 5️⃣ Run the FastAPI app locally

```bash
uvicorn main:app --reload
```

Now open:

```bash
http://127.0.0.1:8000
http://127.0.0.1:8000/docs
```

---

# 🐳 Docker Setup

The project is fully containerized using Docker.

---

## 📦 Build Docker Image

From the project root:

```bash
docker build -t ecommerce-sales-forecast .
```

---

## ▶️ Run Docker Container

```bash
docker run -d -p 8000:8000 --name sales-api ecommerce-sales-forecast
```

---

## 🔍 Check Running Container

```bash
docker ps
```

---

## 📜 View Logs

```bash
docker logs sales-api
```

---

## ⏹️ Stop and Remove Container

```bash
docker stop sales-api
docker rm sales-api
```

---

# 🐳 Docker Compose Setup

Docker Compose was used to simplify container orchestration.

---

## ▶️ Run with Docker Compose

```bash
docker compose up --build
```

### Run in background:
```bash
docker compose up --build -d
```

---

## ⏹️ Stop Compose Services

```bash
docker compose down
```

---

# ☁️ Docker Hub Workflow

This project image has also been pushed to **Docker Hub** for easy pull-and-run usage.

---

## 🔐 Login to Docker Hub

```bash
docker login
```

---

## 🏷️ Tag Docker Image

```bash
docker tag ecommerce-sales-forecast:latest shubham43thakur/ecommerce-sales-forecast:latest
```

### Optional version tag:
```bash
docker tag ecommerce-sales-forecast:latest shubham43thakur/ecommerce-sales-forecast:v1
```

---

## ⬆️ Push to Docker Hub

```bash
docker push shubham43thakur/ecommerce-sales-forecast:latest
docker push shubham43thakur/ecommerce-sales-forecast:v1
```

---

## ⬇️ Pull from Docker Hub

```bash
docker pull shubham43thakur/ecommerce-sales-forecast:latest
```

---

## ▶️ Run Pulled Docker Hub Image

```bash
docker run -d -p 8000:8000 --name sales-api shubham43thakur/ecommerce-sales-forecast:latest
```

Then open:

```bash
http://localhost:8000/docs
```

---


---

# 📈 What This Project Demonstrates

This project showcases:

- Machine Learning model training
- Feature engineering for time-based forecasting
- API development using FastAPI
- Model deployment workflow
- Docker image creation and execution
- Docker Compose orchestration
- Docker Hub image publishing

---


# 👨‍💻 Author

**Shubham Thakur** 

---

# ⭐ If you found this useful.

