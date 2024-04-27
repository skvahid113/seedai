# Crop yield Prediction

This is a FastAPI application for predicting crop yield based on environmental factors using a pre-trained machine learning model.

## Overview

The Crop Prediction API utilizes a PyCaret machine learning model trained on agricultural data to predict the yield of a crop based on various environmental factors such as nitrogen, phosphorus, potassium levels in the soil, temperature, humidity, pH level, and rainfall.

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/sifseedai/seedai.git
    ```

2. Install dependencies:
    ```bash
    pip install streamlit

    pip install fastapi

    pip install pycaret

    pip install uvicorn
    ```

## Usage

1. Start the FastAPI server:
    ```bash
    uvicorn main:app --reload
    ```

2. Once the server is running, you can send POST requests to the `/predict` endpoint with the required input parameters in the request body:
    ```bash
    curl -X 'POST' \
      'http://localhost:8000/predict' \
      -H 'accept: application/json' \
      -H 'Content-Type: application/json' \
      -d '{
      "N": 90,
      "P": 42,
      "K": 43,
      "temperature": 20,
      "humidity": 82,
      "ph": 6,
      "rainfall": 202
    }'
    ```

3. The server will respond with a JSON object containing the predicted crop yield.

## API Documentation

- POST /predict:
  - Description: Predict the yield of a crop based on environmental factors.
  - Request Body Parameters:
    - `N`: Nitrogen level in the soil
    - `P`: Phosphorus level in the soil
    - `K`: Potassium level in the soil
    - `temperature`: Temperature in Celsius
    - `humidity`: Humidity in percentage
    - `ph`: pH level of the soil
    - `rainfall`: Rainfall in mm
  - Response:
    - `prediction`: Predicted crop yield

## Credits

- [PyCaret](https://pycaret.org/): Open-source low-code machine learning library in Python.
- [FastAPI](https://fastapi.tiangolo.com/): FastAPI framework for building APIs with Python 3.7+ based on standard Python type hints.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
