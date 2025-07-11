import re
import joblib
import streamlit as st
from preprocess import preprocess
from ml_training import dummy

def show():
    model = joblib.load("sentiment_analysis/saved/classifier.joblib")
    vectorizer = joblib.load("sentiment_analysis/saved/vectorizer.joblib")

    st.set_page_config(page_title="Sentiment Analysis")
    st.title("Sentiment Analyse für deutsche Texte")

    st.write("Gib einen Text ein, und das Modell sagt dir, ob er **positiv**, **neutral** oder **negativ** ist.")

    text_input = st.text_area("Dein Text:")

    if st.button("Analysieren"):
        if text_input.strip():
            text_lst = preprocess([text_input])
            X = vectorizer.transform(text_lst)
            prediction = model.predict(X)[0]
            st.success(f"📊 Vorhersage: **{prediction.upper()}**")
        else:
            st.warning("Bitte gib einen Text ein.")

if __name__ == "__main__":
    show()
