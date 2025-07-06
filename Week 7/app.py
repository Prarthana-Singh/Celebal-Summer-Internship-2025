#---------------------------------------------------------------------------------------------------
#                     Basic

# import streamlit as st
# import pickle
# import numpy as np
# import pandas as pd
#
# model = pickle.load(open('CarPredModel.pkl','rb'))
# st.header('Car Price Predector')
# Name = st.text_input('Enter the Car name')
# Company = st.text_input('Enter the Company name')
#
# ## Initialize session state
# # if "user_input" not in st.session_state:
# #     st.session_state.user_input = ""
# #
# # # #Create a text input with a placeholder
# # user_input = st.text_input("Enter Year", value=st.session_state.user_input, placeholder="0.00")
#
# # # Update session state when user types
# # if user_input != "0.00":
# #     st.session_state.user_input = user_input
#
# # st.write(f"You entered: {user_input}")
#
#
# Year = st.number_input('Enter Year')
# kms_driven = st.number_input('Enter kms_driven')
# fuel_type = st.selectbox('Enter the fuel type',['Petrol', 'Diesel', 'LPG'])
#
# if st.button('Predict'):
#     prediction = model.predict(pd.DataFrame(columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'],
#                                             data=np.array([Name, Company, Year, kms_driven, fuel_type]).reshape(1, 5)))
#     st.success(prediction)

#------------------------------------------------------------------------------------------------------












import streamlit as st
import pickle
import numpy as np
import pandas as pd
import sklearn

# Load the model
model = pickle.load(open('CarPredModel.pkl', 'rb'))

# Set page configuration
st.set_page_config(page_title="Car Price Predictor", page_icon="🚗", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        padding: 10px 24px;
        border: none;
        border-radius: 4px;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .stTextInput>div>div>input {
        border-radius: 4px;
        border: 1px solid #ccc;
        padding: 8px;
    }
    .stNumberInput>div>div>input {
        border-radius: 4px;
        border: 1px solid #ccc;
        padding: 8px;
    }
    .stSelectbox>div>div>select {
        border-radius: 4px;
        border: 1px solid #ccc;
        padding: 8px;
    }
    </style>
    """, unsafe_allow_html=True)

# Header and description
st.title('🚗 Car Price Predictor')
st.markdown("""
    Welcome to the Car Price Predictor!
    Enter the details of the car below to get an estimated price.
    """)

# Input fields organized into columns
col1, col2 = st.columns(2)

with col1:
    Name = st.text_input('Enter the Car Name', placeholder="e.g., Corolla")
    Company = st.text_input('Enter the Company Name', placeholder="e.g., Toyota")
    Year = st.number_input('Enter the Year', min_value=1900, max_value=2023, step=1, value=2020)

with col2:
    kms_driven = st.number_input('Enter Kilometers Driven', min_value=0, step=1000, value=50000)
    fuel_type = st.selectbox('Enter the Fuel Type', ['Petrol', 'Diesel', 'LPG'])

# Predict button
if st.button('Predict Price'):
    if not Name or not Company:
        st.error("Please fill in all the fields.")
    else:
        try:
            prediction = model.predict(pd.DataFrame(columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'],
                                                    data=np.array([Name, Company, Year, kms_driven, fuel_type]).reshape(1, 5)))
            st.success(f"Predicted Price: ₹{prediction[0]:,.2f}")
        except Exception as e:
            st.error(f"An error occurred: {e}")

# Footer
st.markdown("---")
st.markdown("© 2025 Car Price Predictor. All rights reserved.")














#-----------------------------------------------------------------------------------------
#                               Advanced

# import streamlit as st
# import pickle
# import numpy as np
# import pandas as pd
#
# # Load the model
# model = pickle.load(open('CarPredModel.pkl', 'rb'))
#
# # Set page configuration
# st.set_page_config(page_title="Car Price Predictor 🚗", page_icon="🚗", layout="wide")
#
# # Custom CSS for styling (black background, white text)
# st.markdown("""
#     <style>
#     /* Set Black Background */
#     [data-testid="stAppViewContainer"] {
#         background-color: #000000;
#         color: #FFFFFF;  /* Set default text color to white */
#     }
#     /* Title Style */
#     .title {
#         font-size: 36px;
#         font-weight: bold;
#         color: #FF5733;  /* Bright orange for title */
#         text-align: center;
#         margin-top: 20px;
#     }
#     /* Button Style */
#     .stButton>button {
#         background-color: #FF5733;
#         color: white;
#         font-size: 18px;
#         padding: 10px 24px;
#         border-radius: 8px;
#         cursor: pointer;
#     }
#     .stButton>button:hover {
#         background-color: #FF5733;
#     }
#     /* Input Box Style */
#     .stTextInput>div>div>input, .stNumberInput>div>div>input, .stSelectbox>div>div>select {
#         border-radius: 8px;
#         border: 2px solid #FF5733;
#         padding: 10px;
#         font-size: 16px;
#         background-color: #1E1E1E;  /* Dark input background */
#         color: #FFFFFF;  /* White text */
#     }
#     /* Prediction Box */
#     .pred-box {
#         padding: 15px;
#         background-color: #008000;
#         color: white;
#         font-size: 20px;
#         text-align: center;
#         border-radius: 10px;
#         box-shadow: 2px 2px 10px rgba(0,0,0,0.5);
#         margin-top: 20px;
#     }
#     </style>
#     """, unsafe_allow_html=True)
#
# # Header with Icon
#
#
#
# st.markdown("""
#     <style>
#     @keyframes blink-border {
#         0% { box-shadow: 0px 0px 5px rgba(255, 255, 255, 0.3); }
#         50% { box-shadow: 0px 0px 20px rgba(255, 255, 255, 0.9); }
#         100% { box-shadow: 0px 0px 5px rgba(255, 255, 255, 0.3); }
#     }
#
#     /* Title Banner */
#     .title-box {
#         background: blue; /* Black Background */
#         color: white;
#         font-size: 36px;
#         font-weight: bold;
#         text-align: center;
#         padding: 15px;
#         border-radius: 12px;
#         border: 4px solid white; /* White Bold Border */
#         animation: blink-border 1.5s infinite alternate; /* Blinking Border */
#     }
#     </style>
#     """, unsafe_allow_html=True)
#
# st.markdown('<div class="title-box">🚗 Car Price Predictor</div>', unsafe_allow_html=True)
#
#
# st.markdown("#### *Get an estimated price of your car based on its specifications.*")
#
# # Layout using Columns
# col1, col2 = st.columns([1, 1])
#
# with col1:
#     Name = st.text_input('📝 Enter the Car Name', placeholder="e.g., Corolla")
#     Company = st.text_input('🏭 Enter the Company Name', placeholder="e.g., Toyota")
#     Year = st.number_input('📅 Enter the Year', min_value=1900, max_value=2023, step=1, value=2020)
#
# with col2:
#     kms_driven = st.number_input('📏 Enter Kilometers Driven', min_value=0, step=1000, value=50000)
#     fuel_type = st.selectbox('⛽ Enter the Fuel Type', ['Petrol', 'Diesel', 'LPG'])
#
# # Add an Expander for Additional Info
# with st.expander("ℹ️ **How does this work?**"):
#     st.write("""
#     - This model predicts car prices based on past data.
#     - Fill in the car details, and click "Predict Price".
#     - Our ML model will estimate the best price for your car.
#     """)
#
# # Predict Button with Animation
# if st.button('🔍 Predict Price'):
#     if not Name or not Company:
#         st.error("❌ Please fill in all the fields.")
#     else:
#         with st.spinner("Predicting... ⏳"):
#             try:
#                 prediction = model.predict(pd.DataFrame(columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'],
#                                                         data=np.array([Name, Company, Year, kms_driven, fuel_type]).reshape(1, 5)))
#
#                 st.markdown(f'<div class="pred-box">💰 **Predicted Price: ₹{prediction[0]:,.2f}**</div>', unsafe_allow_html=True)
#             except Exception as e:
#                 st.error(f"❌ An error occurred: {e}")
#
# # Footer with Copyright
# st.markdown("---")
# st.markdown("<p style='text-align:center;'>© 2023 🚗 Car Price Predictor | All rights reserved.</p>", unsafe_allow_html=True)
#
#
#



















