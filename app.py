
import streamlit as st
from transformers import pipeline

# Load sentiment analysis model from Hugging Face
classifier = pipeline('sentiment-analysis')

# Title for the app
st.title("Sentiment Analysis App")
st.markdown("""
This app is a simple, interactive web application built using Streamlit that performs sentiment analysis on user-inputted text using a pre-trained Hugging Face Transformers pipeline.
How It Works:
The app uses the pipeline('sentiment-analysis') function from the transformers library to load a pre-trained sentiment classifier.
Users can input any text into a text area.
Once the input is provided, the app analyzes the sentiment and displays:
The sentiment label (e.g., POSITIVE or NEGATIVE)
A confidence score (ranging from 0 to 1) showing how confident the model is in its prediction.
""")

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
