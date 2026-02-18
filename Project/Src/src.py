Python 3.13.12 (tags/v3.13.12:1cbe481, Feb  3 2026, 18:22:25) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import pandas as pd
... from sklearn.model_selection import train_test_split
... from sklearn.ensemble import RandomForestClassifier
... from sklearn.metrics import accuracy_score
... import joblib
... 
... data = pd.read_csv("data/water_quality_dataset.csv")
... X = data.drop("Disease_Risk", axis=1)
... y = data["Disease_Risk"]
... X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
... model = RandomForestClassifier()
... model.fit(X_train, y_train)
... print("Accuracy:", accuracy_score(y_test, model.predict(X_test)))
... joblib.dump(model, "models/model.pkl")
