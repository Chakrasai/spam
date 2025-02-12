import joblib
import os
from flask import Flask, request, jsonify
from flask_cors import CORS

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

# Load the trained model and vectorizer
MODEL_PATH = os.path.join(BASE_DIR, "model", "model.joblib")
VECTORIZER_PATH = os.path.join(BASE_DIR, "model", "vectorizer.joblib")

try:
    model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VECTORIZER_PATH)
    print("Model and Vectorizer loaded successfully!")
except Exception as e:
    print(f"Error loading model/vectorizer: {e}")
    exit(1)  # Exit if loading fails


@app.route('/')
def home():
    return "Hello, World!"

@app.route('/detectspam', methods=['POST'])
def detect_spam():
    try:
        data = request.json
        text = data.get('text', '')

        if not text:
            return jsonify({'error': 'No text provided'}), 400

        # Transform text using the loaded vectorizer
        text_features = vectorizer.transform([text])

        # Predict spam or not
        prediction = model.predict(text_features)[0]
        result = "Not Spam" if prediction == 1 else "Spam"

        return jsonify({'result': result})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)
