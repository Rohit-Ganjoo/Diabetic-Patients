# diabetes_app/ml_model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

def train_model():
    data = pd.read_csv(r"C:/Users/zeus/Desktop/MeriSKILL/Project 2 Diabetic Patients/diabetes.csv")
    X = data.drop("Outcome", axis=1)
    Y = data['Outcome']
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.4)

    model = LogisticRegression()
    model.fit(X_train, Y_train)

    return model

def predict_diabetes(model, values):
    prediction = model.predict([values])
    return prediction[0]
