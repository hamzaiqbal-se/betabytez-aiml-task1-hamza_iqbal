import streamlit as st
import joblib
import numpy as np

# Load the trained model and scaler
model = joblib.load('water_potability_model.pk1')
scaler = joblib.load('scaler.pk1')

# App title
st.title("💧 Water Potability Prediction")
st.write("Enter the water quality parameters below to check if the water is safe to drink.")

# Input fields for each feature
ph = st.number_input("pH Level", min_value=0.0, max_value=14.0, value=7.0)
hardness = st.number_input("Hardness", min_value=0.0, value=200.0)
solids = st.number_input("Solids (Total Dissolved Solids)", min_value=0.0, value=20000.0)
chloramines = st.number_input("Chloramines", min_value=0.0, value=7.0)
sulfate = st.number_input("Sulfate", min_value=0.0, value=330.0)
conductivity = st.number_input("Conductivity", min_value=0.0, value=420.0)
organic_carbon = st.number_input("Organic Carbon", min_value=0.0, value=14.0)
trihalomethanes = st.number_input("Trihalomethanes", min_value=0.0, value=66.0)
turbidity = st.number_input("Turbidity", min_value=0.0, value=4.0)

# Predict button
if st.button("Predict Potability"):
    # Arrange input into the same order as training data
    input_data = np.array([[ph, hardness, solids, chloramines, sulfate,
                             conductivity, organic_carbon, trihalomethanes, turbidity]])
    
    # Note: Random Forest was trained on unscaled data, so we use input_data directly
    prediction = model.predict(input_data)[0]
    
    if prediction == 1:
        st.success("✅ This water is predicted to be POTABLE (safe to drink).")
    else:
        st.error("❌ This water is predicted to be NOT POTABLE (unsafe to drink).")