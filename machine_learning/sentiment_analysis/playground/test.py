import streamlit as st

st.title("Sentiment Prediction App")

text = st.text_input("Enter your text:")

if st.button("Analyze"):
    # fake prediction
    st.write("Prediction: Positive")