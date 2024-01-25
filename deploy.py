import streamlit as st
import pandas as pd
import pickle

# Load the saved model
model_filename = 'Linear Regression_best_model.pkl'  # Change this to your actual filename

try:
    with open(model_filename, 'rb') as model_file:
        model = pickle.load(model_file)
except FileNotFoundError:
    st.error("Model file not found. Please ensure the correct filename.")


location_mapping = {'Mumbai': 0, 'Delhi': 1, 'Kolkata': 2}
fuel_type_mapping = {'Petrol':0, 'Diesel':1, 'CNG':2}
transmission_mapping = {'Manual':0, 'Automatic':1}
owner_type_mapping = {'First':0, 'Second':0, 'Third':0}

# Streamlit app
st.title('Car Price Prediction')


# Input parameters
location = st.selectbox('Location', ['Mumbai', 'Delhi', 'Kolkata'])
year = st.slider('Year', 2000, 2022, 2010)
kilometers_driven = st.number_input('Kilometers Driven', min_value=0)
fuel_type = st.selectbox('Fuel Type', ['Petrol', 'Diesel', 'CNG'])
transmission = st.selectbox('Transmission', ['Manual', 'Automatic'])
owner_type = st.selectbox('Owner Type', ['First', 'Second', 'Third'])
mileage = st.number_input('Mileage', min_value=0.0)
engine = st.number_input('Engine', min_value=0.0)
power = st.number_input('Power', min_value=0.0)
seats = st.slider('Seats', 1, 10, 5)
brand = st.text_input('Brand')

location_int = location_mapping.get(location, 0)
fuel_int = fuel_type_mapping.get(fuel_type,0)
transmission_int = transmission_mapping.get(transmission,0)
owner_type_int = owner_type_mapping.get(owner_type,0)

# User input DataFrame
input_data = pd.DataFrame({
    'Location': [location_int],
    'Year': [year],
    'Kilometers_Driven': [kilometers_driven],
    'Fuel_Type': [fuel_int],
    'Transmission': [transmission_int],
    'Owner_Type': [owner_type_int],
    'Mileage': [mileage],
    'Engine': [engine],
    'Power': [power],
    'Seats': [seats],
    'Brand': [brand]
})

# Make prediction
if st.button('Predict Price'):
    try:
        prediction = model.predict(input_data)
        st.success(f'Predicted Price: {prediction[0]:,.2f} INR')
    except Exception as e:
        st.error(f"Prediction error: {str(e)}")
