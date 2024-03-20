import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model_filename = 'regression.joblib'
model = joblib.load(model_filename)

# Streamlit application
st.title('BMI Prediction App')

# User input for gender
gender = st.radio('Select Gender:', ['Male', 'Female'])

# User input for height
height = st.number_input('Enter Height (cm):', min_value=50, max_value=250, value=170)

# User input for weight
weight = st.number_input('Enter Weight (kg):', min_value=1, max_value=500, value=70)

# Encode gender
gender_encoder = {'Male': 0, 'Female': 1}
gender_encoded = gender_encoder[gender]

# Create a DataFrame with user input
user_data = pd.DataFrame({
    'Gender': [gender_encoded],
    'Height': [height],
    'Weight': [weight]
})

# Make prediction
prediction = model.predict(user_data)[0]

# Decode the predicted BMI category
bmi_categories = ['Extremely Weak', 'Weak', 'Normal', 'Overweight', 'Obesity', 'Extremely Obesity']
predicted_category = bmi_categories[prediction]

# Display the prediction
st.subheader('Prediction:')
st.success(f'The predicted BMI category is: **{predicted_category}**')
