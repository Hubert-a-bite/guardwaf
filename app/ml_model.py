import pickle
import os

clf = None
vec = None

def load_model():
    global clf, vec
    if clf is None or vec is None:
        with open("ml/model.pkl", "rb") as f:
            clf = pickle.load(f)
        with open("ml/vectorizer.pkl", "rb") as f:
            vec = pickle.load(f)

def predict_ml(query: str) -> bool:
    load_model()
    X = vec.transform([query])
    return clf.predict(X)[0] == 1
