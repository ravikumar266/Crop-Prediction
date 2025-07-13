import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/predict"

st.title("Crop Predicter")

st.header("Enter the details below to predict the crop")

Temperature=st.number_input("Temperature in celsius",min_value=0,max_value=100, value=23 )
Humidity = st.number_input("Humidity in air", min_value=0,max_value=100)
Rainfall=st.number_input("Rainfall in mm",min_value=0, value=200 )
PH=st.number_input("PH",min_value=0,max_value=14, value=7 )
Nitrogen=st.number_input("Nitrogen content in soil",min_value=0,value=40 )
Phosphorous=st.number_input("Phosphorous content in soil",min_value=0, value=23 )
Potassium=st.number_input("Potassium content in Soil",min_value=0,value=23 )
Carbon=st.number_input("Carbon in Soil",min_value=0, value=23 )
Acidic_Soil=st.selectbox("'Acidic_soli' Choose 0 for no 1 for yes", [0,1] )
Alkaline_Soil=st.selectbox("'Alkaline_Soil' Choose 0 for no 1 for yes", [0,1] )
Loamy_Soil=st.selectbox("'Loamy_Soil' Choose 0 for no 1 for yes", [0,1] )
Neutral_Soil=st.selectbox("'Neutral_Soil' Choose 0 for no 1 for yes", [0,1] )
Peaty_Soil=st.selectbox("'Peaty_Soil' Choose 0 for no 1 for yes", [0,1] )



if st.button("Predict Crop"):
    payload = {
        "Temperature": Temperature,
        "Humidity": Humidity,
        "Rainfall": Rainfall,
        "PH": PH,
        "Nitrogen": Nitrogen,
        "Phosphorous": Phosphorous,
        "Potassium": Potassium,
        "Carbon": Carbon,
        "Acidic_Soil": Acidic_Soil,
        "Alkaline_Soil": Alkaline_Soil,
        "Loamy_Soil": Loamy_Soil,
        "Neutral_Soil": Neutral_Soil,
        "Peaty_Soil": Peaty_Soil
    }

    try:

       response = requests.post(API_URL, json=payload)

       if response.status_code == 200:
          prediction = response.json().get("predicted_crop")
          st.success(f"The predicted crop is: {prediction}")
       else:
           st.error(f"Error: {response.json().get('detail', 'Unknown error')}")


    except requests.exceptions.ConnectionError:
        st.error(" Could not connect to FastAPI server at 127.0.0.1:8000")
