# ☀️ Solar Energy Forecasting using Machine Learning

A machine learning project that predicts solar energy generation using weather data. The project compares multiple regression models and deploys the best-performing model using Streamlit.

---

## 📌 Project Overview

This project uses historical weather data to forecast solar energy generation. Various machine learning algorithms were trained and evaluated, with **XGBoost Regressor** selected as the final model due to its superior performance.

---

## 🚀 Features

- Solar Energy Prediction
- Weather Data Analysis
- Data Preprocessing
- Feature Engineering
- Model Comparison
- XGBoost Regression
- Random Forest Regression
- Streamlit Web Application
- Interactive User Interface

---

## 📂 Project Structure

```
Solar-Farm-Forecasting/
│
├── app.py
├── requirements.txt
├── scaler.pkl
├── solar.ipynb
├── solar.pbix
├── solar_energy_model_lr.pkl
├── solar_energy_model_rf.joblib
├── solar_energy_model_xgb.joblib
├── solar_energy_predictions.csv
├── solar_weather.csv
└── README.md
```

---

## 📊 Dataset Features

| Feature | Description |
|----------|-------------|
| GHI | Global Horizontal Irradiance |
| temp | Temperature |
| pressure | Atmospheric Pressure |
| humidity | Humidity |
| wind_speed | Wind Speed |
| rain_1h | Rainfall (1 hour) |
| snow_1h | Snowfall (1 hour) |
| clouds_all | Cloud Coverage |
| isSun | Sun Visibility |
| sunlightTime | Sunlight Time |
| dayLength | Length of Day |
| SunlightTime/daylength | Sunlight Ratio |
| weather_type | Weather Category |
| hour | Hour of Day |

**Target Variable**

- Energy

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Joblib
- Streamlit
- Power BI
- Jupyter Notebook

---

## 🤖 Machine Learning Models

- Linear Regression
- Random Forest Regressor
- XGBoost Regressor ✅ (Best Model)

---

## 📈 Evaluation Metrics

- R² Score
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/solar-farm-forecasting.git
```

Move into the project folder

```bash
cd solar-farm-forecasting
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Streamlit application

```bash
streamlit run app.py
```

---

## 💻 Streamlit Dashboard

The dashboard allows users to:

- Enter weather parameters
- Predict solar energy generation
- View input data
- Get real-time predictions

---

## 📁 Model Files

| File | Description |
|------|-------------|
| solar_energy_model_xgb.joblib | Final XGBoost Model |
| solar_energy_model_rf.joblib | Random Forest Model |
| solar_energy_model_lr.pkl | Linear Regression Model |
| scaler.pkl | Feature Scaler |

---

## 📊 Power BI Dashboard

The repository also includes a Power BI dashboard for data visualization.

```
solar.pbix
```

---

## Future Improvements

- Hyperparameter Optimization
- Model Explainability (SHAP)
- Real-time Weather API Integration
- Cloud Deployment
- Automated Retraining Pipeline

---

## 👨‍💻 Author

**Eshat**

Computer Science & Engineering Student

Interested in:

- Artificial Intelligence
- Machine Learning
- Data Science
- Deep Learning

---

## ⭐ If you found this project helpful, please give it a Star!
