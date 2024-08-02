# importing python libraries and methods
import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model
import streamlit as st

# Load word index and reverse word index
word_index = imdb.get_word_index()
reverse_word_index = {value: key for key, value in word_index.items()}

# Load trained model
model = load_model('123.h5')

# Decode review function
def decode_review(encoded_review):
    return ' '.join([reverse_word_index.get(i - 3, '?') for i in encoded_review])

# Preprocess text function
def preprocess_text(text):
    words = text.lower().split()
    encoded_review = [word_index.get(word, 2) + 3 for word in words]
    padded_review = pad_sequences([encoded_review], maxlen=500)
    return padded_review

# Prediction function
def predict_sentiment(review):
    preprocessed_input = preprocess_text(review)
    prediction = model.predict(preprocessed_input)
    score = prediction[0][0]
    if score > 0.5:
        sentiment = "positive"
        emoji = "😊"
    elif 0.27 < score <= 0.5:
        sentiment = "neutral"
        emoji = "😐"
    else:
        sentiment = "negative"
        emoji = "😞"
    return sentiment, emoji, score

# Streamlit app
st.title("Movie Sentiment Analysis")
st.subheader("Enter a movie review to predict its sentiment")

# User input
user_input = st.text_area("Movie Review")

if st.button('Classify...'):
    if user_input.strip():
        # Predict sentiment
        sentiment, emoji, score = predict_sentiment(user_input)
        
        # Display results
        st.markdown(f'### The movie review is : **{sentiment}**', unsafe_allow_html=True)
        st.markdown(f'# --{emoji}--', unsafe_allow_html=True)
        st.markdown(f'### Prediction score: **{score:.2f}**', unsafe_allow_html=True)
    else:
        st.write('Please enter a valid review.')
else:
    st.write('Enter a movie review and click "Classify..." to get the sentiment analysis.')
