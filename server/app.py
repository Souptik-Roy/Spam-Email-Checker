# already deploy in render
from flask import Flask, request, jsonify, render_template
import pickle
from flask_cors import CORS   # <-- add this

app = Flask(__name__)
CORS(app)  # <-- enable CORS for all routes

# Load trained pipeline
with open("spam-checker-pipeline.pkl", "rb") as f:
    spam_clf = pickle.load(f)

# Root route (so "/" works too, not just /index.html)
@app.route('/')
@app.route('/index.html')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    message = data.get("message", "").strip()

    if message == "":
        return jsonify({"error": "Please enter a message before checking."}), 400

    prediction = spam_clf.predict([message])[0]
    result = "Spam" if prediction == 1 else "Not Spam"
    return jsonify({"prediction": result})

if __name__ == '__main__':
    app.run(debug=True)
