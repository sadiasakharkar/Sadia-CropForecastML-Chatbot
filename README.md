# Sadia's-CropForecastML-Chatbot
A machine learning-based platform for forecasting crop yields. Leverages data-driven models to predict agricultural outcomes and support effective farming strategies.

# AgriYield Pro 🌾🤖

CropYieldPredictor is a machine learning project designed to predict agricultural crop yields using advanced predictive analytics. The goal is to provide accurate forecasts based on historical data, helping farmers and agricultural professionals make informed decisions and optimize their farming practices.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Model Details](#model-details)
- [Contributing](#contributing)
- [Contact](#contact)

## Introduction

Agriculture is a vital sector that requires accurate methods for predicting crop yields. Sadia's Crop-Forecast ML Pro aims to revolutionize the agriculture industry by providing precise predictions based on historical data and real-time inputs. This tool helps mitigate risks associated with farming and improves food security by making the agricultural sector more resilient and sustainable.

## Features

- **Predict Crop Yields**: Utilize advanced machine learning algorithms to predict crop yields accurately.
- **User-Friendly Interface**: An intuitive interface for inputting data and viewing predictions.
- **AI-Powered Insights**: Leverage AI to support agricultural productivity.
- **No API Key Required**: Seamless access without needing an API key.

## Installation

To run this project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/sadiasakharkar/CropForecastML.git
   cd AgriYield-Pro

2. **Install dependencies:**
    bash
   
       pip install -r requirements.txt

4. Ensure model file:
    Place the trained model file dtr (1).pkl in the project directory.


## Usage 

   Start the application by running:
   
    ```bash
       streamlit run web_app.py

   Input Features
    Year: Year for which crop yield prediction is required.
    Average Rainfall (mm per year): Annual average rainfall in millimeters.
    Pesticides (tonnes): Quantity of pesticides used in tonnes.
    Average Temperature (°C): Average temperature in degrees Celsius.
    Area: Select the geographic area from the provided options.
    Item: Choose the type of crop from the available options.

   Example
   After launching the Streamlit app, input the required features and click "Predict" to view the    predicted    crop yield.



## Model Details
The prediction model used is a Decision Tree Regressor trained on historical crop yield data. The dtr (1).pkl file contains the model parameters and is loaded during runtime to predict crop yields based on user inputs.  

## Contributing
Contributions are welcome! For suggestions or improvements, feel free to create an issue or submit a pull request adhering to the project's coding standards.

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your branch to your fork.
5. Open a pull request with a clear description of your changes.

## Contact
For any questions or feedback, please contact sakharkarsadia@gmail.com
