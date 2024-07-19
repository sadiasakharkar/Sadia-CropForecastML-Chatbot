import streamlit as st
import pickle
import numpy as np

# Load the pre-trained model and preprocessor
with open('/Users/doctor/App_crop-yield/dtr.pkl', 'rb') as model_file:
    dtr = pickle.load(model_file)

with open('/Users/doctor/App_crop-yield/preprocessor.pkl', 'rb') as preprocessor_file:
    preprocesser = pickle.load(preprocessor_file)




# Define the prediction function
def prediction(average_rain_fall_mm_per_year, pesticides_tonnes, avg_temp, Area, Item):
    # Create an array of the input features
    features = np.array([[average_rain_fall_mm_per_year, pesticides_tonnes, avg_temp, Area, Item]], dtype=object)

    # Transform the features using the preprocessor
    transformed_features = preprocesser.transform(features)

    # Make the prediction
    predicted_yield = dtr.predict(transformed_features).reshape(1, -1)

    return predicted_yield[0]

# Streamlit app
st.title('Agricultural Yield Prediction')

st.sidebar.header('Input Parameters')

Year = st.sidebar.number_input('Year', min_value=1900, max_value=2100, value=1990)
average_rain_fall_mm_per_year = st.sidebar.number_input('Average Rainfall (mm per year)', min_value=0.0, value=1485.0)
pesticides_tonnes = st.sidebar.number_input('Pesticides (tonnes)', min_value=0.0, value=121.0)
avg_temp = st.sidebar.number_input('Average Temperature (°C)', value=16.37)
Area = st.sidebar.text_input('Area', value='Albania')
Item = st.sidebar.text_input('Item', value='Maize')

if st.sidebar.button('Predict'):
    result = prediction(average_rain_fall_mm_per_year, pesticides_tonnes, avg_temp, Area, Item)
    st.write(f'The predicted yield for {Item} in {Area} for the year {Year} is {result:.2f}')
    