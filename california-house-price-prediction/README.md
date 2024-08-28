# California House Price Prediction

This project is an end-to-end machine learning solution for predicting housing prices in California. The application is built using FastAPI for serving the machine learning model and Docker for containerization, ensuring easy deployment and scalability.

## Table of Contents
- [Project Overview](#project-overview)
- [Software Architecture](#software-architecture)
- [How to Run Locally](#how-to-run-locally)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)

## Project Overview
The California House Price Prediction project aims to predict housing prices based on various features such as location, median income, housing age, and more. This application uses a pre-trained machine learning model, which is served through a FastAPI backend. The entire application is containerized using Docker for easy deployment.

## Software Architecture
### 1. **Data Preprocessing and Model Training**
   - **Data Preprocessing**: The dataset is cleaned and processed using techniques like handling missing values with `SimpleImputer`, scaling numerical features with `StandardScaler`, and encoding categorical variables with `OneHotEncoder`.
   - **Model Training**: A regression model (e.g., Random Forest, Linear Regression) is trained on the processed dataset to predict housing prices.

### 2. **API Service (FastAPI)**
   - The trained model is loaded into a FastAPI application.
   - An endpoint (`/predict`) is provided for making predictions. The endpoint accepts JSON input containing features and returns the predicted house prices.

### 3. **Containerization (Docker)**
   - The FastAPI application is containerized using Docker, ensuring consistency across different environments.
   - The Docker image includes all necessary dependencies and is configured to expose the API on port 80.

### **Design Choices**
- **FastAPI** was chosen for its high performance, ease of use, and automatic generation of API documentation.
- **Docker** ensures that the application can be easily deployed and run in any environment without worrying about dependencies.
- **Pydantic** is used for data validation in FastAPI to ensure that the input data adheres to the expected schema.

## How to Run Locally

### Prerequisites
- **Docker**: Ensure Docker is installed on your machine.
- **Python 3.11+** (if you want to run the application without Docker).

### Steps to Run with Docker
1. **Clone the Repository**
   ```bash
   git clone https://github.com/avinwu/ds_projects.git
   cd california-house-price-prediction

2. Make sure docker service is running. In Windows start the Docker Desktop.


3. **Build the Docker Image**
    ```bash
    docker build -t california-house-price-prediction .
   
4. **Run the Docker Container**
    ```bash
   docker run -p 80:80 california-house-price-prediction

## **Usage**
### Sample Request
```json
[
  {
    "longitude": -119.01,
    "latitude": 36.06,
    "housing_median_age": 25.0,
    "total_rooms": 1505.0,
    "total_bedrooms": 120.0,
    "population": 1392.0,
    "households": 359.0,
    "median_income": 1.6812,
    "ocean_proximity": "INLAND"
  }
]
```
### Sample Response
```json
{
  "predicted_price": [123456.78]
}
```

### Sample Python Code
```python
import requests

url = "http://localhost:8000/predict"

data = [{
    "longitude": -122.23,
    "latitude": 37.88,
    "housing_median_age": 41.0,
    "total_rooms": 880.0,
    "total_bedrooms": 129.0,
    "population": 322.0,
    "households": 126.0,
    "median_income": 8.3252,
    "ocean_proximity": "NEAR BAY"
}]

response = requests.post(url, json=data)
print(response.json())
```
## Project Structure
```bash
california-house-price-prediction/
│
├── app.py                 # FastAPI application code
├── housing_prices.ipynb   # Jupyter notebook for model training
├── regressor.pkl          # Pre-trained model file
├── Dockerfile             # Docker configuration
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```
**Note** - Pre-trained model file `regressor.pkl` could not be uploaded to github because of 25M file restriction. If required, it can be regenerated using the model serialization step.
## Dependencies
- Python 3.11+
- FastAPI
- Uvicorn
- Joblib
- Pandas
- Scikit-learn
- Docker

## Conclusion
This project demonstrates a full pipeline for deploying a machine learning model using modern tools like FastAPI and Docker. The architecture is designed to be scalable and easy to deploy, making it suitable for production environments.
