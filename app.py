import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load('mobile_price_model.pkl')

st.title("📱 Mobile Price Prediction App")
st.write("Enter the mobile specifications to get an estimated price.")

# Input fields
ram_gb = st.number_input("RAM (GB)", min_value=1, max_value=32, value=8)
rom_gb = st.number_input("ROM (GB)", min_value=8, max_value=1024, value=128)
display_inch = st.number_input("Display Size (inch)", min_value=4.0, max_value=8.0, value=6.5)
main_cam_mp = st.number_input("Main Camera (MP)", min_value=2, max_value=200, value=50)
rating = st.number_input("Rating", min_value=1.0, max_value=5.0, value=4.5, step=0.1)
has_discount = st.selectbox("Has Discount?", [0, 1])
brand = st.selectbox("Brand", ['Apple', 'Samsung', 'Google', 'OnePlus', 'Xiaomi', 'Motorola', 'Other'])

# Predict button
if st.button("Predict Price"):
    input_df = pd.DataFrame({
        'RAM_GB': [ram_gb],
        'ROM_GB': [rom_gb],
        'Display_inch': [display_inch],
        'Main_Cam_MP': [main_cam_mp],
        'Rating': [rating],
        'Has_Discount': [has_discount],
        'Brand': [brand]
    })
    
    predicted_price = model.predict(input_df)[0]
    st.success(f"Estimated Selling Price: ₹{predicted_price:,.0f}")
