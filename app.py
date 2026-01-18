from flask import Flask, render_template, request
import joblib
import numpy as np
from feature_extraction import extract_features

app = Flask(__name__)

# Load the trained model
try:
    model = joblib.load('fraud_model.pkl')
except FileNotFoundError:
    print("Error: fraud_model.pkl not found. Please run train_model.py first!")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    url = request.form['url']
    
    # 1. Extract features using your Phase 2 script
    features = extract_features(url)
    
    # 2. Convert to numpy array and reshape for the model
    # Note: You can ignore the "UserWarning" about feature names; 
    # it doesn't stop the code from working.
    features_array = np.array(features).reshape(1, -1)
    
    # 3. Get the raw prediction (e.g., 'phishing' or 'legitimate')
    # WE REMOVED int() FROM HERE
    raw_prediction = model.predict(features_array)[0]
    
    # 4. Determine if it is fraud based on the string result
    is_fraud = False
    if str(raw_prediction).lower() in ['phishing', '1', 'bad', 'fraud']:
        is_fraud = True

    # 5. Send the boolean 'is_fraud' to your HTML template
    return render_template('index.html', url=url, result=is_fraud)

if __name__ == "__main__":
    app.run(debug=True)