import streamlit as st
import pickle
import numpy as np

# Load your model (adjust the path accordingly)
model_path = 'model (1).pkl'
with open(model_path, 'rb') as model_file:
    model = pickle.load(model_file)

# Title of the app
st.title("Car Model Prediction")

# Input features
feature1 = st.text_input("Enter Feature 1:")
feature2 = st.text_input("Enter Feature 2:")
feature3 = st.text_input("Enter Feature 3:")

# Button for prediction
if st.button("Predict"):
    # Convert features to a numpy array
    features = np.array([[float(feature1), float(feature2), float(feature3)]])
    
    # Make prediction
    prediction = model.predict(features)
    
    # Display the prediction
    st.write(f"The predicted value is : {prediction[0]}")
