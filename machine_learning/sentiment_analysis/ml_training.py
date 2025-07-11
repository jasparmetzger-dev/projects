import os
import joblib
import pandas as pd
from preprocess import load_data

df = pd.read_csv(os.path.join(os.getcwd(), "sentiment_analysis", "data", "train_data.csv"))
file_path = "sentiment_analysis/saved/preprocessed_data.joblib"

def dummy(x):
    return x

def vectorize(data_list: list[list[str]]):
    from sklearn.feature_extraction.text import TfidfVectorizer

    print("[INFO] vectorizing...")
    vectorizer = TfidfVectorizer(ngram_range= (1, 1),  #param
                                 analyzer= dummy,
                                 token_pattern= None,
                                 max_features= 20000,
                                 min_df= 3)
    
    X = vectorizer.fit_transform(data_list)
    return X, vectorizer

def classify(X, Y):
    from sklearn.linear_model import LogisticRegression

    print("[INFO] classifiying data...")
    model = LogisticRegression(max_iter= 1000, C= 1)
    model.fit(X, Y)
    return model

def train():

    #data, labels = load_data(file_path)
    data = load_data(file_path)
    labels = df["sentiment"].tolist()
    X, vectorizer = vectorize(data)
    clf = classify(X, labels)

    print("[INFO] saving...")
    joblib.dump(vectorizer, "sentiment_analysis/saved/vectorizer.joblib")
    joblib.dump(clf, "sentiment_analysis/saved/classifier.joblib")

    print("[INFO] save successfull!")

def tune():
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.linear_model import LogisticRegression
    from sklearn.pipeline import Pipeline
    from sklearn.model_selection import GridSearchCV
    from sklearn.metrics import classification_report
    import joblib

    print("[INFO] loading data...")
    data = load_data(file_path)
    labels = df["sentiment"].to_list()

    print("[INFO] building pipeline...")
    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer(analyzer= dummy,
                                 max_features= 5000,
                                 token_pattern= None,
                                 lowercase= False)),
        ('clf', LogisticRegression(max_iter=1000))
        ])
    param_grid = {
        'tfidf__max_features': [3000, 5000, 10000, 20000],
        'clf__C': [0.01, 0.1, 1, 10],
        'clf__class_weight': [None, 'balanced'],
        'tfidf__min_df': [1, 3, 5]
    }

    print("[INFO] optimizing...")
    grid = GridSearchCV(pipeline, param_grid, cv=5, scoring='f1_macro', n_jobs=-1)
    grid.fit(data, labels)

    print("[INFO] Best Params:", grid.best_params_)
    print("[INFO] downloading...")
    joblib.dump(grid.best_estimator_, "sentiment_analysis/saved/best_sentiment_model.joblib")

if __name__ == "__main__":
    train()