import streamlit as st
import requests

# Define the Streamlit app
def main():
    st.title('Crop Yield Prediction')

    # Add input fields for user to enter data
    st.sidebar.header('Enter Data:')
    N_info = "Nitrogen (N) is a crucial nutrient for plant growth and development. It helps in the formation of proteins, enzymes, and chlorophyll."
    N = st.sidebar.number_input('Nitrogen (N) ', min_value=0, help=N_info)

    P_info = "Phosphorus (P) is important for photosynthesis, energy transfer, and the development of roots and flowers."
    P = st.sidebar.number_input('Phosphorus (P)  ', min_value=0, help=P_info)

    K_info = "Potassium (K) is essential for plant growth and plays a key role in regulating water uptake and photosynthesis."
    K = st.sidebar.number_input('Potassium (K)  ', min_value=0, help=K_info)

    temperature_info = "Temperature affects plant metabolism and growth rates. Different crops have specific temperature requirements for optimal growth."
    temperature = st.sidebar.number_input('Temperature  ', min_value=0.0, help=temperature_info)

    humidity_info = "Humidity influences transpiration rates and water uptake by plants. It can affect plant health and susceptibility to diseases."
    humidity = st.sidebar.number_input('Humidity  ', min_value=0.0, help=humidity_info)

    ph_info = "pH level of the soil affects nutrient availability to plants. Most crops grow best in slightly acidic to neutral soils."
    ph = st.sidebar.number_input('pH  ', min_value=0.0, help=ph_info)

    rainfall_info = "Rainfall provides water essential for plant growth. Insufficient or excessive rainfall can affect crop yield."
    rainfall = st.sidebar.number_input('Rainfall  ', min_value=0.0, help=rainfall_info)

    # When the user clicks the 'Predict' button, perform prediction
    if st.sidebar.button('Predict'):
        # Send HTTP request to FastAPI server
        response = requests.post("http://34.170.154.42/predict",
                                params={"N": N, "P": P, "K": K,
                                        "temperature": temperature,
                                        "humidity": humidity, "ph": ph,
                                        "rainfall": rainfall})
        if response.status_code == 200:
            predicted_yield = response.json()["prediction"]
            st.write(f'Predicted Crop Yield: {predicted_yield}')
        else:
            st.error("Failed to get prediction from server.")

if __name__ == '__main__':
    main()
