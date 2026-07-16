import streamlit as st
import pandas as pd
import joblib
import os

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="Solar Energy Prediction",
    page_icon="☀️",
    layout="wide"
)

st.title("☀️ Solar Energy Prediction Dashboard")
st.write("Predict Solar Energy Generation using the trained XGBoost Model.")

# ----------------------------
# Load Model & Scaler
# ----------------------------
@st.cache_resource
def load_files():
    model = joblib.load("solar_energy_model_xgb.joblib")
    scaler = joblib.load("scaler.pkl")
    return model, scaler

try:
    model, scaler = load_files()
except Exception as e:
    st.error(f"Error Loading Model: {e}")
    st.stop()

# ----------------------------
# Sidebar Inputs
# ----------------------------
st.sidebar.header("Input Features")

GHI = st.sidebar.number_input("GHI", value=100.0)
temp = st.sidebar.number_input("Temperature (°C)", value=25.0)
pressure = st.sidebar.number_input("Pressure", value=1013.0)
humidity = st.sidebar.slider("Humidity (%)", 0, 100, 50)
wind_speed = st.sidebar.number_input("Wind Speed", value=2.0)
rain_1h = st.sidebar.number_input("Rain (1h)", value=0.0)
snow_1h = st.sidebar.number_input("Snow (1h)", value=0.0)
clouds_all = st.sidebar.slider("Cloud Cover (%)", 0, 100, 20)
isSun = st.sidebar.selectbox("Is Sun Visible?", [0, 1])
sunlightTime = st.sidebar.number_input("Sunlight Time", value=300.0)
dayLength = st.sidebar.number_input("Day Length", value=700.0)
ratio = st.sidebar.number_input(
    "SunlightTime / DayLength",
    value=sunlightTime / dayLength if dayLength != 0 else 0.0
)
weather_type = st.sidebar.number_input("Weather Type", value=1)
hour = st.sidebar.slider("Hour", 0, 23, 12)

# ----------------------------
# Create DataFrame
# ----------------------------
input_df = pd.DataFrame({
    "GHI":[GHI],
    "temp":[temp],
    "pressure":[pressure],
    "humidity":[humidity],
    "wind_speed":[wind_speed],
    "rain_1h":[rain_1h],
    "snow_1h":[snow_1h],
    "clouds_all":[clouds_all],
    "isSun":[isSun],
    "sunlightTime":[sunlightTime],
    "dayLength":[dayLength],
    "SunlightTime/daylength":[ratio],
    "weather_type":[weather_type],
    "hour":[hour]
})

st.subheader("Input Data")
st.dataframe(input_df)

# ----------------------------
# Prediction
# ----------------------------
if st.button("Predict Solar Energy"):

    scaled_input = scaler.transform(input_df)

    prediction = model.predict(scaled_input)[0]

    st.success(f"Predicted Solar Energy: **{prediction:.2f}**")

# ----------------------------
# Footer
# ----------------------------
st.markdown("---")
st.caption("Developed using Streamlit & XGBoost")