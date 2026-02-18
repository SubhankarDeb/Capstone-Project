Python 3.13.12 (tags/v3.13.12:1cbe481, Feb  3 2026, 18:22:25) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import streamlit as st
... import joblib
... import numpy as np
... 
... model = joblib.load("models/model.pkl")
... 
... st.title("Waterborne Disease Prediction System")
... pH = st.slider("pH Level", 0.0, 14.0, 7.0)
... ...
... if st.button("Predict"):
...     input_data = np.array([[pH, turbidity, oxygen, temp, nitrate, bacteria, rainfall, population]])
...     result = model.predict(input_data)
