# Filpkart Smartphone Web Scrapping and Price Prediction

📱 Mobile Price Prediction

📌 Project Overview
This project predicts the selling price of mobile phones based on their specifications such as RAM, ROM, display size, camera megapixels, brand, rating, and discount status.
The dataset was scraped from e-commerce product listings, cleaned, processed, and used to train machine learning models.

We deployed the final model using Streamlit so users can interactively input mobile specifications and get an estimated selling price.

📊 Dataset
Final features used:

RAM_GB — RAM in GB

ROM_GB — Internal storage in GB

Display_inch — Display size in inches

Main_Cam_MP — Main camera resolution in megapixels

Rating — Customer rating

Has_Discount — 1 if the product has a discount, else 0

Brand — Mobile phone brand

Target Variable: Selling Price Num — Selling price in INR

🧠 Models Trained
We tested multiple regression models:

Model	MAE	RMSE	R²

Linear Regression	8079.43	12686.65	0.7955

Random Forest	5873.46	9565.39	0.8837

Gradient Boosting	4691.48	8478.12	0.9086

Final chosen model: GradientBoostingRegressor (best performance)

🛠 Tech Stack
Python
Selenium, Beautiful Soup - Web Scrapping

Pandas, NumPy — Data processing

Scikit-learn — Machine learning

Matplotlib, Seaborn, Plotly — Data visualization

Streamlit — Deployment

Joblib — Model persistence

🚀 Deployment Guide
1️⃣ Train and Save the Model
bash
Copy
Edit
python train_model.py
This saves the model as mobile_price_model.pkl.

2️⃣ Run the Streamlit App
bash
Copy
Edit
streamlit run app.py
📂 File Structure
bash
Copy
Edit
📦 mobile-price-prediction
├── final_mobile_data.csv     # Cleaned dataset
├── train_model.py            # Model training and saving
├── app.py                    # Streamlit application
├── mobile_price_model.pkl    # Saved trained model
├── README.md                 # Project documentation
🎯 How It Works
User enters mobile specifications in the Streamlit app.

The trained machine learning pipeline preprocesses inputs.

The Gradient Boosting model predicts the estimated price.

The predicted price is displayed in INR.

📌 Future Improvements
Allow users to choose between models in the UI.

Deploy the app to Streamlit Cloud or Render.

Improve predictions by adding more features like battery capacity, processor type, etc.

Do you want me to now add the multiple model selection feature in the Streamlit app so it looks more professional and interactive?
It will make your README and app even better.
