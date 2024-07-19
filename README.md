# Sadia-CropForecastML-Chatbot
A machine learning-based platform for forecasting crop yields. Leverages data-driven models to predict agricultural outcomes and support effective farming strategies.

# AgriYield Pro 🌾🤖

Welcome to Sadia's Crop-Forecast ML Pro! This project leverages advanced AI and machine learning algorithms to provide farmers with precise crop yield predictions. It's designed to assist farmers in making informed decisions, optimizing resource usage, and ultimately enhancing agricultural productivity.

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
   git clone https://github.com/sadiasakharkar/AgriYield-Pro.git
   cd AgriYield-Pro

2. **Install dependencies:**
    bash
    pip install -r requirements.txt

3. Ensure model file:
    Place the trained model file dtr (1).pkl in the project directory.


## Usage 

    Start the application by running:
    ```bash
       streamlit run app.py

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

## Contact
Email sakharkarsadia@gmail.com for questions, feedback, or collaborations.
