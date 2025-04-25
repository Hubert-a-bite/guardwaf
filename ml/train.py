import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
import pickle
import os

os.makedirs("ml", exist_ok=True)

data = pd.DataFrame({
    "query": [
        "id=1", "user=admin' --", "<script>alert(1)</script>",
        "../../etc/passwd", "ls -la; whoami", "q=hello world"
    ],
    "label": [0, 1, 1, 1, 1, 0]
})

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(data["query"])
y = data["label"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
clf = MultinomialNB()
clf.fit(X_train, y_train)

with open("ml/model.pkl", "wb") as f:
    pickle.dump(clf, f)
with open("ml/vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("Trained model.")
