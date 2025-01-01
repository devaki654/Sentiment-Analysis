### Sentiment Analysis Project

#### Description:
This project implements sentiment analysis using a pre-trained Keras model to classify input text as either positive or negative. The Flask-based web application provides a user-friendly interface where users can input text and receive sentiment predictions.

---

### README

## Sentiment Analysis Web Application

### Overview:
This project leverages a pre-trained Keras model to perform sentiment analysis on user-provided text. Using Flask for the web framework, users can easily input text, and the application will predict whether the sentiment is positive or negative. The model is trained to classify sentiments based on textual input, offering a straightforward and interactive way to analyze sentiment.

### Features:
- **User-Friendly Web Interface**: Users can input text and receive sentiment predictions.
- **Real-Time Sentiment Prediction**: The model predicts whether the input text is positive or negative.
- **Pre-Trained Model**: The sentiment analysis model is trained using Keras and loaded dynamically for prediction.
- **Flask Web Application**: The app is built with Flask to allow for simple deployment and interaction.

### Requirements:
- **Python 3.x** or higher
- **Flask**: Python framework for web development
- **TensorFlow/Keras**: For model loading and prediction
- **NumPy**: For numerical operations
- **h5py**: To load Keras models saved in `.h5` or `.keras` format

### Installation:

1. **Clone the repository** or download the source code:
   ```bash
   git clone https://github.com/your-username/sentiment-analysis-web-app.git
   cd sentiment-analysis-web-app
   ```

2. **Set up a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Download the pre-trained model** (`sentiment_analysis_model.keras`) and place it in the project directory.

5. **Run the Flask app**:
   ```bash
   python app.py
   ```

6. **Open the application in a browser**:
   Navigate to `http://127.0.0.1:5000/` to access the web application.

### File Structure:
```
/sentiment-analysis-web-app
│
├── app.py                        # Main Flask application script
├── sentiment_analysis_model.keras # Pre-trained sentiment analysis model
├── templates
│   └── index.html                 # HTML template for the web interface
└── requirements.txt               # Required Python packages
```

### Usage:
1. Open the app in your browser at `http://127.0.0.1:5000/`.
2. Enter the text you want to analyze in the provided text box.
3. Press the "Analyze" button to submit the text for sentiment prediction.
4. The sentiment will be displayed as either **Positive** or **Negative**.

### Example Input:
- "I absolutely love this product! It works perfectly."
- "The service is terrible. I'm never coming back."

### Example Output:
- **Positive**
- **Negative**

### Troubleshooting:
- **Model file not found**: If you receive an error related to the model not being found, ensure the model file (`sentiment_analysis_model.keras`) exists in the project directory.
- **Missing dependencies**: If you encounter errors related to missing libraries, verify that you've installed all dependencies by running `pip install -r requirements.txt`.

### Contributing:
If you would like to contribute to this project, feel free to fork the repository and submit pull requests. You can also open issues to report bugs or suggest improvements.

---

This README provides everything needed to set up, use, and contribute to your Sentiment Analysis Web Application project.
