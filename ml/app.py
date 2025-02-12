from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

model = joblib.load(r"C:\Users\chakr\OneDrive\Desktop\mern\spam\ml\model\model.joblib")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    text = data["text"]
    prediction = model.predict([text])[0]
    return jsonify({"prediction": "spam" if prediction == 1 else "Not Spam"})

if __name__ == "__main__":
    app.run(port=5001)

import joblib
from flask import Flask, request, jsonify
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

# Load the trained model and vectorizer
model_path = r'C:\Users\chakr\OneDrive\Desktop\mern\spam\ml\model\model.joblib'
vectorizer_path = r'C:\Users\chakr\OneDrive\Desktop\mern\spam\ml\model\vectorizer.joblib'

try:
    model = joblib.load(model_path)
    vectorizer = joblib.load(vectorizer_path)
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

