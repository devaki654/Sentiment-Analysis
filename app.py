from flask import Flask, render_template, request
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np

# Initialize Flask app
app = Flask(__name__)

import os

# Verify if the model file exists before loading it
model_path = r"C:\Users\cuted\Desktop\deep in\sentiment_analysis_model.keras"
if os.path.exists(model_path):
    model = load_model(model_path)
else:
    print("Model file not found!")

# Assuming the model was trained with these parameters (you can adjust this if different)
max_len = 100  # Maximum length for padding
tokenizer = Tokenizer(num_words=5000)

# Define a route for the homepage
@app.route('/')
def home():
    return render_template('index.html')

# Define a route to handle form submissions
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get the text entered by the user
        text = request.form['text']
        
        # Preprocess the text
        sequences = tokenizer.texts_to_sequences([text])
        padded = pad_sequences(sequences, maxlen=max_len)

        # Predict sentiment (positive or negative)
        prediction = model.predict(padded)
        
        # Assuming the model outputs a value between 0 and 1 for positive sentiment
        sentiment = 'Positive' if prediction >= 0.5 else 'Negative'

        return render_template('index.html', prediction_text=f'Sentiment: {sentiment}')

if __name__ == "__main__":
    app.run(debug=True)
