# Crop-Prediction
Crop Prediction Project


# 🌾 Crop Prediction Web Application

This is a full-stack machine learning web application that predicts the most suitable crop based on environmental and soil parameters. It uses **FastAPI** for the backend and **Streamlit** for the frontend.

---

## 📌 Features

- Predicts crop using input features like temperature, humidity, pH, nutrients, and soil type.
- Backend built with **FastAPI** to handle model inference and API communication.
- Frontend built using **Streamlit** for an interactive UI.
- Real-time crop prediction using a trained ML model.
- Clean and modern UI (dark theme enabled).

---

##  Tech Stack

| Component    | Technology     |
|--------------|----------------|
| Backend API  | FastAPI        |
| Frontend     | Streamlit      |
| ML Model     | scikit-learn   |
| Data Handling| Pandas, NumPy  |

---

##  Input Parameters

| Parameter           | Description                          |
|---------------------|--------------------------------------|
| Temperature         | In Celsius                           |
| Humidity            | In %                                 |
| Rainfall            | In mm                                |
| PH                  | pH level of the soil (0–14)          |
| Nitrogen            | Nitrogen content in soil             |
| Phosphorous         | Phosphorous content in soil          |
| Potassium           | Potassium content in soil            |
| Carbon              | Carbon content in soil               |
| Acidic_Soil         | 1 if acidic, else 0                  |
| Alkaline_Soil       | 1 if alkaline, else 0                |
| Loamy_Soil          | 1 if loamy, else 0                   |
| Neutral_Soil        | 1 if neutral, else 0                 |
| Peaty_Soil          | 1 if peaty, else 0                   |

---

##  How to Run the Project

### 1. Clone the Repository

```bash
git  git clone https://github.com/ravikumar266/Crop-Prediction.git


cd Crop-Prediction

### creating virtual envirment

python -m venv venv
# For Windows
venv\Scripts\activate
# For Mac/Linux
source venv/bin/activate

## install dependecies

pip install -r requirements.txt

##  Run the Backend (FastAPI)

cd app

uvicorn main:app --reload

##  Run the Frontend (Streamlit)   open new terminal but not close old terminal 

cd Crop-Prediction ## if required

cd streamlit

streamlit run frontend.py








