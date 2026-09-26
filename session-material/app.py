import streamlit as st 
import requests


st.set_page_config(page_title="Predictor")

experience = st.number_input("Experience in Years", 
                min_value=0.0,
                max_value=10.0,
                value=1.0,
                step=.5)



if st.button("Predict Salary"):
    # prediction = model.predict(experience)
    url = "http://127.0.0.1:8000/predict"
    response = requests.post(url, json={"experience_years": experience})

    if response.status_code == 200:
        result = response.json()
        st.success(f"Predicted Salary: {result['predicted_salary']}")