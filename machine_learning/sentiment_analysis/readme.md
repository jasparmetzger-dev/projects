# Sentiment Analysis

This project implements a German-language sentiment analysis system using classical machine learning methods.  
It processes German text inputs and predicts if the sentiment is **positive**, **neutral**, or **negative**.

## Features
- Text preprocessing tailored for German language
- Trained classification model with sklearn
- Streamlit-based interactive UI for user input and prediction

## Usage
Run the Streamlit app to analyze your text sentiment interactively.
Command: streamlit run sentiment_analysis/app.py

## Folder Structure
- `app.py` — Main app entry point  
- `preprocess.py` — Text preprocessing functions  
- `ml_training.py` — Model training script  
- `saved/` — Stored vectorizer and model artifacts  
- `data/` — Training and test datasets

## Implemtation

- using the TF-IDF Vectorizer for NLP
- using a Logistic-Regression-Model for the classifier
- preprocessing using Lemmatization
- tuning with gridsearch, although the model is not really optimmized

## Weaknesses of the model
- due to no usage of n-grams, e.g. double negatives will not be recognised and thus falsly interpreted
- the model as a whole is fairly simple and easy to break
- it only has an accuracy of 80% because of this

---

