import streamlit as st
import pandas as pd
import numpy as np
import joblib


model = joblib.load('readmission_model.pkl')
label_encoders = joblib.load('label_encoders.pkl')
feature_names = joblib.load('model_features.pkl')

st.title("🏥 Hospital Readmission Predictor")


age = st.number_input("Age", min_value=0, max_value=120)
gender = st.selectbox("Gender", ['Male', 'Female'])
condition = st.selectbox("Medical Condition", ['Diabetes', 'Hypertension', 'Heart Disease', 'Asthma', 'Other'])
treatment = st.selectbox("Treatment Type", ['Medication', 'Surgery', 'Therapy', 'Other'])
stay_days = st.slider("Length of Stay (in days)", 1, 60)


input_dict = {
    'age': age,
    'gender': gender,
    'medical_condition': condition,
    'treatment': treatment,
    'length_of_stay': stay_days
}


input_df = pd.DataFrame([input_dict])


for col in input_df.columns:
    if col in label_encoders:
        le = label_encoders[col]
        try:
            input_df[col] = le.transform(input_df[col])
        except ValueError:
            st.warning(f"⚠️ '{input_df[col].values[0]}' not seen during training in column '{col}'. Using default.")
            default_value = 'Other' if 'Other' in le.classes_ else le.classes_[0]
            input_df[col] = le.transform([default_value])


feature_names = joblib.load('model_features.pkl')  
input_df_full = pd.DataFrame(columns=feature_names)
input_df_full.loc[0] = 0  # Initialize all with 0


for col in input_df.columns:
    if col in input_df_full.columns:
        input_df_full.at[0, col] = input_df.at[0, col]


if st.button("Predict Readmission"):
    prediction = model.predict(input_df_full)[0]
    if prediction == 1:
        st.error("⚠️ Patient is likely to be readmitted within 30 days.")
    else:
        st.success("✅ Patient is not likely to be readmitted.")

