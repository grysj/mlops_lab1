import os
import joblib
import pandas as pd
from training import load_data, train_model, save_model


def load_model():
    if os.path.exists("model.pkl"):
        model = joblib.load("model.pkl")
    else:
        X, y = load_data()
        model = train_model(X, y)
        save_model(model)

    return model


def predict(model, data):
    data = pd.DataFrame([data])
    pred = model.predict(data)
    return pred[0]
