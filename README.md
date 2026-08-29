# House Price Prediction

## Project Description

This project predicts house prices using Machine Learning.

A Linear Regression model is used to predict the sale price of a house based on:

- Square Footage
- Number of Bedrooms
- Number of Bathrooms

## Features Used

| Feature | Dataset Column |
|---|---|
| Square Footage | GrLivArea |
| Bedrooms | BedroomAbvGr |
| Bathrooms | FullBath |
| Target | SalePrice |

## Machine Learning Model

The project uses Linear Regression from Scikit-learn.

### Model Performance

- MAE: 35788.06
- MSE: 2806426667.25
- RMSE: 52975.72
- R² Score: 0.6341

The R² score of 0.6341 means that the model explains approximately 63.41% of the variation in house prices using the selected features.

## Streamlit Application

The project includes a Streamlit web application where users can enter:

1. Square footage
2. Number of bedrooms
3. Number of bathrooms

The application then predicts the estimated house price.

## Project Structure
```text
TASK_01_HOUSE_PRICE_PREDICTION/
│
├── data/
│   └── train.csv
│
├── model/
│   └── House_price_linear_regression.pkl
│
├── notebooks/
│   └── task_01.ipynb
│
├── app.py
├── README.md
├── requirements.txt
├── sample_submission.csv
├── submission.csv
└── test.csv
# 🏠 House Price Prediction

Predict house prices using Linear Regression based on square footage, number of bedrooms, and number of bathrooms.
## 🔗 Project Links

### 📂 GitHub Repository

<https://github.com/Hariram-ai/SCT_ML_1>

### 🚀 Live Demo

<https://sctml1-n4rovk68iqye7axwxpgwcw.streamlit.app>
