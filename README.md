Phishing URL Detection System using Machine Learning :

 Project Abstract:

In the modern digital landscape, phishing attacks remain a critical threat to cybersecurity. This project implements an intelligent system capable of identifying fraudulent websites in real-time. Unlike traditional signature-based detection (blacklisting), this system uses a Random Forest Classifier to analyze the structural and behavioral features of a URL. By extracting key indicators such as domain length, special character frequency, and security protocols, the model can detect "Zero-Day" phishing sites with high accuracy.


Features:

Real-time Analysis: Instant classification of URLs as "Safe" or "Fraudulent."

Machine Learning Based: Utilizes a Random Forest algorithm trained on thousands of labeled URLs. (raw data used from https://www.kaggle.com/datasets/sid321axn/malicious-urls-dataset)


Feature Extraction: Custom Python logic to analyze URL components (TLD, Subdomains, Path).

User-Friendly Interface: A clean, responsive web dashboard built with Flask.

 Tech Stack:
Language: Python 3.x

Machine Learning: Scikit-learn, Pandas, NumPy

Web Framework: Flask (Python)

Frontend: HTML5, CSS3

Model Serialization: Joblib (Pickle)


URL Parsing: tldextract


 Project Structure:

Plaintext

URLFraudDetection/
├── app.py                  # Main Flask application
├── feature_extraction.py   # URL attribute extraction logic
├── train_model.py         # Script to train and save the ML model
├── fraud_model.pkl         # Trained model file (serialized)
├── processed_data.csv      # Cleaned data used for training
├── requirements.txt        # List of dependencies
└── templates/
    └── index.html          # Web application UI


 Installation & Setup:

1. Clone the Repository
Bash

git clone https://github.com/athira-byte/URLFraudDetection.git
cd URLFraudDetection
2. Install Dependencies
Bash

pip install -r requirements.txt
3. Generate the Model (Optional)
If the fraud_model.pkl is not present (due to GitHub file size limits), run the training script:

Bash

python train_model.py
4. Run the Application
Bash

python app.py
Open your browser and navigate to http://127.0.0.1:5000


 System Architecture
The system follows a standard 3-tier architecture:

Client Tier: User submits a URL via the browser.

Server Tier: Flask extracts features and passes them to the ML model.

Intelligence Tier: Random Forest Classifier determines the safety score based on trained patterns.

Future Scope:

Browser Extension: Porting the logic to a Chrome/Firefox extension for passive protection.

Deep Learning: Implementing LSTM or CNN models for character-level URL analysis.

Live Database: Integrating with APIs like Google Safe Browsing for hybrid verification.

Author:

Adarsh K Das 

MCA Final Year
Amrita vishwa Vidyapeetham
aa.sc.p2mca2401047@ahead.students.amrita.edu
