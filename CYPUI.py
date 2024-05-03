import streamlit as st
import requests

# Dictionary mapping crop label to crop name
crop_names = {
    0: 'apple',
    1: 'banana',
    2: 'blackgram',
    3: 'chickpea',
    4: 'coconut',
    5: 'coffee',
    6: 'cotton',
    7: 'grapes',
    8: 'jute',
    9: 'kidneybeans',
    10: 'lentil',
    11: 'maize',
    12: 'mango',
    13: 'mothbeans',
    14: 'mungbean',
    15: 'muskmelon',
    16: 'orange',
    17: 'papaya',
    18: 'pigeonpeas',
    19: 'pomegranate',
    20: 'rice',
    21: 'watermelon'
}

# Additional information about each crop
crop_info = {
    'rice': 'Rice is a staple food for more than half of the world\'s population, providing essential nutrients and energy. It is consumed in various forms and is a significant source of carbohydrates.',
    'maize': 'Maize, also known as corn, is one of the most widely cultivated cereal grains in the world. It is a versatile crop used for food, animal feed, and industrial products such as ethanol and biofuel.',
    'chickpea': 'Chickpea is a nutritious legume rich in protein, fiber, vitamins, and minerals. It is a staple food in many parts of the world and is used in a variety of dishes such as curries, salads, and soups.',
    'kidneybeans': 'Kidney beans are a rich source of protein, fiber, and essential nutrients. They are commonly used in various cuisines around the world, including soups, stews, salads, and chili.',
    'pigeonpeas': 'Pigeon peas, also known as arhar dal or tur dal, are a nutritious legume widely cultivated in tropical and subtropical regions. They are an important source of protein and are used in various culinary dishes such as curries, soups, and stews.',
    'mothbeans': 'Moth beans, also known as matki or Turkish gram, are a small, drought-resistant legume cultivated in arid and semi-arid regions. They are a good source of protein, fiber, and essential nutrients.',
    'mungbean': 'Mung beans, also known as green gram, are a nutritious legume commonly used in Asian cuisine. They are rich in protein, fiber, vitamins, and minerals, and are used in various dishes such as soups, salads, and curries.',
    'blackgram': 'Black gram, also known as urad dal or black lentils, is a highly nutritious pulse commonly used in Indian cuisine. It is rich in protein, fiber, and essential nutrients, and is used in dishes such as dals, curries, and idlis.',
    'lentil': 'Lentils are a versatile and nutritious pulse commonly used in cuisines around the world. They are rich in protein, fiber, vitamins, and minerals, and are used in various dishes such as soups, stews, salads, and curries.',
    'pomegranate': 'Pomegranate is a delicious and nutritious fruit known for its juicy arils and sweet-tart flavor. It is rich in antioxidants, vitamins, and minerals, and is believed to offer several health benefits, including improved heart health and reduced inflammation.',
    'banana': 'Bananas are one of the most popular fruits worldwide, known for their sweet taste, creamy texture, and high nutritional value. They are rich in essential vitamins, minerals, and antioxidants, and are a good source of energy.',
    'mango': 'Mango is a tropical fruit prized for its sweet, juicy flesh and rich flavor. It is rich in vitamins, minerals, and antioxidants, and is enjoyed fresh or used in various culinary dishes such as smoothies, desserts, and salads.',
    'grapes': 'Grapes are delicious and nutritious fruits known for their juicy flesh, sweet flavor, and versatility. They are rich in vitamins, minerals, and antioxidants, and are enjoyed fresh as a snack or used in various culinary dishes such as salads, desserts, and juices.',
    'watermelon': 'Watermelon is a refreshing and hydrating fruit known for its juicy flesh and sweet flavor. It is low in calories and rich in vitamins, minerals, and antioxidants, making it a healthy and delicious addition to any diet.',
    'muskmelon': 'Muskmelon, also known as cantaloupe or sweet melon, is a delicious and nutritious fruit prized for its sweet flavor and juicy flesh. It is rich in vitamins, minerals, and antioxidants, and is enjoyed fresh or used in various culinary dishes such as salads, smoothies, and desserts.',
    'apple': 'Apples are crisp, juicy fruits known for their sweet-tart flavor and nutritional benefits. They are rich in vitamins, minerals, and antioxidants, and are enjoyed fresh as a snack or used in various culinary dishes such as pies, sauces, and salads.',
    'orange': 'Oranges are juicy citrus fruits known for their refreshing flavor and high vitamin C content. They are rich in vitamins, minerals, and antioxidants, and are enjoyed fresh as a snack or used in various culinary dishes such as juices, salads, and desserts.',
    'papaya': 'Papaya is a tropical fruit prized for its sweet flavor, vibrant color, and numerous health benefits. It is rich in vitamins, minerals, and antioxidants, and is enjoyed fresh or used in various culinary dishes such as salads, smoothies, and desserts.',
    'coconut': 'Coconut is a versatile fruit known for its sweet flavor and rich texture. It is used in various culinary dishes such as curries, desserts, and beverages, and is prized for its nutritional benefits, including its high content of healthy fats and minerals.',
    'cotton': 'Cotton is a valuable crop known for its soft, fluffy fibers, which are used to make textiles, clothing, and other products. It is cultivated in many parts of the world and plays a significant role in the global economy.',
    'jute': 'Jute is a natural fiber derived from the stem of the jute plant. It is known for its strength, durability, and eco-friendly properties, and is used to make various products such as bags, rugs, and textiles.',
    'coffee': 'Coffee is one of the most popular beverages in the world, prized for its rich flavor, aroma, and caffeine content. It is made from roasted coffee beans and is enjoyed by millions of people worldwide as a morning pick-me-up or a social drink.'
}

# Display the title
st.markdown("<h1 class='title'>Crop Prediction</h1>", unsafe_allow_html=True)

# Define the Streamlit app
def main():
    st.markdown("""
    <style>
    /* Center-align the title */
    .title {
        text-align: center;
        color: #2C3E50; /* Dark blue color for title */
        font-size: 36px; /* Increase font size for title */
        font-weight: bold; /* Make title bold */
        margin-bottom: 30px; /* Add margin for spacing */
    }
    
    /* Style for predicted crop */
    .predicted-crop {
        font-size: 28px; /* Decrease font size for predicted crop */
        color: #27AE60; /* Green color for predicted crop */
        text-align: center;
        margin-top: 20px; /* Add margin for spacing */
    }
    
    /* Style for crop description */
    .crop-description {
        font-size: 16px; /* Decrease font size for crop description */
        color: #34495E; /* Dark gray color for crop description */
        text-align: center;
        margin-top: 20px; /* Add margin for spacing */
        background-color: #EAEDED; /* Light gray background for crop description */
        padding: 20px; /* Add padding for spacing */
        border-radius: 10px; /* Add border radius for rounded corners */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Add shadow for depth */
    }
    
    /* Style for sidebar header */
    .sidebar-header {
        font-size: 20px; /* Increase font size for sidebar header */
        color: #333333; /* Dark gray color for sidebar header */
        margin-bottom: 15px; /* Add margin for spacing */
    }
    
    /* Style for sidebar input fields */
    .sidebar-input {
        margin-bottom: 25px; /* Add margin for spacing */
    }
    
    /* Style for range messages */
    .range-message {
        font-size: 14px; /* Decrease font size for range messages */
        margin-top: 5px; /* Add margin for spacing */
    }
    
    /* Style for predict button */
    .predict-button {
        background-color: #2980B9; /* Blue color for predict button */
        color: white; /* White text color for predict button */
        font-size: 18px; /* Increase font size for predict button */
        font-weight: bold; /* Make predict button text bold */
        padding: 10px 20px; /* Add padding for predict button */
        border-radius: 5px; /* Add border radius for rounded corners */
        margin-top: 20px; /* Add margin for spacing */
        text-align: center; /* Center-align the text */
        cursor: pointer; /* Change cursor to pointer */
        width: 100%; /* Set button width to 100% */
    }
    
    /* Hover effect for predict button */
    .predict-button:hover {
        background-color: #3498DB; /* Darker blue color on hover */
    }
    </style>
    """, unsafe_allow_html=True)

    # Add input fields for user to enter data
    st.sidebar.markdown("<h3 class='sidebar-header'>Select Parameters:</h3>", unsafe_allow_html=True)

    # Define information tooltips for each input field
    N_info = "Nitrogen (N) is a crucial nutrient for plant growth and development. It aids in the formation of proteins, enzymes, and chlorophyll."
    P_info = "Phosphorus (P) is important for photosynthesis, energy transfer, and the development of roots and flowers."
    K_info = "Potassium (K) is essential for plant growth and plays a key role in regulating water uptake and photosynthesis."
    temperature_info = "Temperature affects plant metabolism and growth rates. Different crops have specific temperature requirements for optimal growth."
    humidity_info = "Humidity influences transpiration rates and water uptake by plants. It can affect plant health and susceptibility to diseases."
    ph_info = "The pH level of the soil affects nutrient availability to plants. Most crops grow best in slightly acidic to neutral soils."
    rainfall_info = "Rainfall provides essential water for plant growth. Insufficient or excessive rainfall can adversely affect crop yield."

    # Define the input fields with appropriate ranges and tooltips
    col1, col2 = st.sidebar.columns(2)
    with col1:
        N = st.slider('Nitrogen (N) (mg/Kg or mg/L)', min_value=0, max_value=140, value=0, help=N_info, key='N')
        st.markdown("<p class='range-message'>Acceptable range: 0-140</p>", unsafe_allow_html=True)
        P = st.slider('Phosphorus (P) (mg/Kg or mg/L)', min_value=5, max_value=145, value=5, help=P_info, key='P')
        st.markdown("<p class='range-message'>Acceptable range: 5-145</p>", unsafe_allow_html=True)
        K = st.slider('Potassium (K) (mg/Kg or mg/L)', min_value=5, max_value=205, value=5, help=K_info, key='K')
        st.markdown("<p class='range-message'>Acceptable range: 5-205</p>", unsafe_allow_html=True)
    with col2:
        temperature = st.slider('Temperature (°C)', min_value=2, max_value=44, value=2, help=temperature_info, key='temperature')
        st.markdown("<p class='range-message'>Acceptable range: 2-44°C</p>", unsafe_allow_html=True)
        humidity = st.slider('Humidity (% RH)', min_value=14, max_value=100, value=14, help=humidity_info, key='humidity')
        st.markdown("<p class='range-message'>Acceptable range: 14%-100%</p>", unsafe_allow_html=True)
        ph = st.slider('pH', min_value=3.5, max_value=10.0, value=3.5, help=ph_info, key='ph')
        st.markdown("<p class='range-message'>Acceptable range: 3.5-10.0</p>", unsafe_allow_html=True)
        rainfall = st.slider('Rainfall (mm)', min_value=20, max_value=300, value=20, help=rainfall_info, key='rainfall')
        st.markdown("<p class='range-message'>Acceptable range: 20-300 mm</p>", unsafe_allow_html=True)

    # Style the predict button
    if st.sidebar.button('Predict', key='predict_button'):
        if N < 0 or N > 140:
            st.sidebar.error("Nitrogen (N) value must be between 0 and 140.")
        elif P < 5 or P > 145:
            st.sidebar.error("Phosphorus (P) value must be between 5 and 145.")
        elif K < 5 or K > 205:
            st.sidebar.error("Potassium (K) value must be between 5 and 205.")
        elif temperature < 2 or temperature > 44:
            st.sidebar.error("Temperature value must be between 2°C and 44°C.")
        elif humidity < 14 or humidity > 100:
            st.sidebar.error("Humidity value must be between 14% and 100%.")
        elif ph < 3.5 or ph > 10:
            st.sidebar.error("pH value must be between 3.5 and 10.")
        elif rainfall < 20 or rainfall > 300:
            st.sidebar.error("Rainfall value must be between 20 mm and 300 mm.")
        else:
            # Send HTTP request to FastAPI server
            response = requests.post("http://34.170.154.42/predict",
                                     params={"N": N, "P": P, "K": K,
                                             "temperature": temperature,
                                             "humidity": humidity, "ph": ph,
                                             "rainfall": rainfall})
            if response.status_code == 200:
                predicted_yield = response.json()["prediction"]
                # Map predicted label to crop name
                predicted_crop = crop_names.get(predicted_yield)
                if predicted_crop is not None:
                   st.markdown(f'<div class="predicted-crop" style="font-size: 36px; color: #FF5733; font-weight: bold;">{predicted_crop}</div>', unsafe_allow_html=True)
                   st.markdown(f'<div class="crop-description" style="font-size: 18px;">{crop_info.get(predicted_crop, "No additional information available.")}</div>', unsafe_allow_html=True)

                else:
                    st.error("Failed to map prediction to crop name.")
            else:
                st.error("Failed to get prediction from server.")

if __name__ == '__main__':
    main()
