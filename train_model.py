import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib

def train_fraud_detector():
    # 1. Load the processed data
    df = pd.read_csv('processed_data.csv')
    
    # 2. Separate Features (X) and Target Label (y)
    X = df.drop('label', axis=1)
    y = df['label']
    
    # 3. Split into Training (80%) and Testing (20%) sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    print("Training the model... please wait.")
    
    # 4. Initialize and Train Random Forest
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # 5. Evaluate the Model
    predictions = model.predict(X_test)
    print("\nModel Accuracy:", accuracy_score(y_test, predictions))
    print("\nDetailed Report:\n", classification_report(y_test, predictions))
    
    # 6. Save the model and the column names for the web app
    joblib.dump(model, 'fraud_model.pkl')
    print("\nModel saved as 'fraud_model.pkl'")

if __name__ == "__main__":
    train_fraud_detector()