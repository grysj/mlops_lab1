from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import joblib

from api.models.iris import PredictRequest


def load_data():
    dataset = load_iris(as_frame=True)
    X = dataset.data
    # there is possibly more elegant way to do this, but hey it wotks
    X.columns = list(PredictRequest.model_fields)
    y = dataset.target_names[dataset.target]
    return X, y


def train_model(X, y):
    model = RandomForestClassifier()
    model.fit(X, y)
    return model


def save_model(model, filename="model.pkl"):
    joblib.dump(model, filename)
