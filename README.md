# IMDB Sentimental Analysis with Simple RNN

This repository contains a Streamlit application for predicting the sentiment of movie reviews using a Simple RNN model.
The model has been trained on the IMDB dataset, and the application allows users to input their own reviews to get sentiment predictions.

Features:
  Sentiment Analysis: Predicts whether a given movie review is positive or negative.
  Review Decoding: Converts the encoded review back to its original text form for better visualization.
  
How to Run the Application:
  1. Clone the repository: git clone [^1^][1]
  2. Navigate to the cloned directory: cd IMDB-Sentimental-Analysis-Simple-RNN
  3. Download the pre-trained model (RNN_model.h5) and place it in the root directory.
  4. Run the Streamlit application: streamlit run app.py
     
Usage:
Enter a movie review in the provided text area.
Click on the “Predict” button to get the sentiment prediction (Positive ,Negative, Nutral).

Code Overview (app.py):
  1. Load the pre-trained model: my_model = load_model('123.h5')
  2. Preprocessing and decoding functions:
      * decode_review(encoded_review): Converts encoded review to text.
      * preprocess_text(text): Preprocesses input text for prediction.
  3. Predict sentiment function: predict_sentiment(text)
Feel free to explore the code and adapt it for your own projects! 🚀

GitHub Repository : https://github.com/Tushar365/Movie-Sentiment-Analysis

Let me know if you need any further assistance! 😊
