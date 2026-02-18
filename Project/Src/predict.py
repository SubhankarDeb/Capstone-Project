Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import joblib
... import numpy as np
... 
... model = joblib.load("models/model.pkl")
... sample = np.array([[7.2, 3.0, 6.0, 26, 12, 60, 150, 350]])
... prediction = model.predict(sample)
... print("High Risk" if prediction[0] == 1 else "Low Risk")
