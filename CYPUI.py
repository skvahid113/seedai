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

# Define the Streamlit app
def main():
    st.markdown("""
    <style>
    /* Center-align the title */
    .title {
        text-align: center;
        color: #ff5733; /* Change the color to your preferred color */
    }
    </style>
    """, unsafe_allow_html=True)

# Display the title
    st.markdown("<h1 class='title'>Crop Yield Prediction</h1>", unsafe_allow_html=True)


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

    # Add input fields for other parameters

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
            # Map predicted label to crop name
            predicted_crop = crop_names.get(predicted_yield)
            if predicted_crop is not None:
               
                st.markdown(f'<font size="+8">**Predicted Crop: <font size="+20" color="#85FFBD">{predicted_crop}</font>**</font>', unsafe_allow_html=True)
                st.write(f'<font size="+10" color="#1A42CE">Description:  {crop_info.get(predicted_crop, "No additional information available.")}</font>', unsafe_allow_html=True)

                # Print input values for other parameters
            else:
                st.error("Failed to map prediction to crop name.")
        else:
            st.error("Failed to get prediction from server.")

if __name__ == '__main__':
    main()
