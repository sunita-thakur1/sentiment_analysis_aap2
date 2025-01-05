
        
import streamlit as st
from transformers import pipeline

# Load sentiment analysis model from Hugging Face
classifier = pipeline('sentiment-analysis')

# Title for the app
st.title("Sentiment Analysis App")

# User input section
text = st.text_area("Enter text for sentiment analysis:")

if text:
    # Perform sentiment analysis
    result = classifier(text)
    sentiment = result[0]['label']
    score = result[0]['score']

    # Display the result
    st.write(f"Sentiment: {sentiment}")
    st.write(f"Confidence Score: {score:.2f}")
