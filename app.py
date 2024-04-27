from fastapi import FastAPI
from pycaret.classification import load_model, predict_model
import pandas as pd
import uvicorn
import json

# Define FastAPI app
app = FastAPI()

# Load the trained PyCaret model
model = load_model('seedai_cyp')

# Define prediction endpoint
@app.post("/predict")
async def predict(N: float, P: float, K: float, temperature: float, humidity: float, ph: float, rainfall: float):
    input_features = pd.DataFrame({'N': [N],
                                   'P': [P],
                                   'K': [K],
                                   'temperature': [temperature],
                                   'humidity': [humidity],
                                   'ph': [ph],
                                   'rainfall': [rainfall]})
    prediction = predict_model(model, data=input_features)
    predicted_label = prediction.iloc[0]['prediction_label']  # Assuming the column name for the prediction is 'Label'
    return {"prediction": predicted_label}

# Run the FastAPI app with uvicorn
if __name__ == '__main__':
    import nest_asyncio
    nest_asyncio.apply()
    app.run(host="0.0.0.0", port=8080)
