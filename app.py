import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("model/House_price_linear_regression.pkl")

# Page configuration
st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="centered"
)

# Title
st.title("🏠 House Price Prediction")

st.write(
    "Predict the price of a house based on its "
    "square footage, bedrooms, and bathrooms."
)

st.success("Model loaded successfully!")

# Input section
st.subheader("Enter House Details")

square_feet = st.number_input(
    "Square Footage",
    min_value=100,
    max_value=6000,
    value=1500,
    step=50
)

bedrooms = st.number_input(
    "Number of Bedrooms",
    min_value=1,
    max_value=10,
    value=3,
    step=1
)

bathrooms = st.number_input(
    "Number of Bathrooms",
    min_value=1,
    max_value=5,
    value=2,
    step=1
)

# Prediction
if st.button("Predict House Price"):

    input_data = pd.DataFrame({
        "GrLivArea": [square_feet],
        "BedroomAbvGr": [bedrooms],
        "FullBath": [bathrooms]
    })

    prediction = model.predict(input_data)

    st.success(
        f"Estimated House Price: ${prediction[0]:,.2f}"
    )
    # Model information
st.divider()

st.subheader("About the Model")

st.write(
    "This application uses Linear Regression to predict house prices "
    "based on square footage, number of bedrooms, and number of bathrooms."
)

st.info(
    "Model R² Score: 0.6341. "
    "The prediction is an estimate and may differ from the actual market price."
)