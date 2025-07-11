import os
import joblib
import pandas as pd
from preprocess import load_data
from ml_training import dummy

df = pd.read_csv(os.path.join(os.getcwd(), "sentiment_analysis", "data", "test_data.csv"))
file_path = "sentiment_analysis/saved/preprocessed_testing_data.joblib"
#file_path = "best_sentiment_model.joblib"
def test():
    def predict(clf, vectorizer, data, labels):
        from sklearn.metrics import classification_report, confusion_matrix
        from sklearn.feature_extraction.text import TfidfVectorizer

        print("[INFO] prediciting...")

        X = vectorizer.transform(data)
        predictions = clf.predict(X)

        cr = classification_report(labels, predictions)
        cm = confusion_matrix(labels, predictions)
        return cr, cm


    print("[INFO] loading model and vectorizer...")

    clf = joblib.load("sentiment_analysis/saved/classifier.joblib")
    vectorizer = joblib.load("sentiment_analysis/saved/vectorizer.joblib")

    print("[INFO] load preprocessed data...")

    data = load_data(file_path)
    label = df["sentiment"].tolist()[:len(data)]
    return predict(clf, vectorizer, data, label)

if __name__ == "__main__":
    cr, cm = test()
    print(cr, cm)