import pandas as pd
import numpy as np
from feature_extraction import extract_features  # Importing your Phase 2 script

def collect_and_prepare_data(input_file, output_file):
    print("--- Starting Data Collection & Feature Extraction ---")
    
    # 1. Load the raw dataset
    # Expected CSV format: [url, label]
    try:
        df = pd.read_csv(input_file)
    except FileNotFoundError:
        print(f"Error: {input_file} not found. Please download your dataset first.")
        return

    print(f"Total URLs to process: {len(df)}")

    # 2. Extract features for every URL in the list
    # We create a list of feature vectors
    print("Extracting features... (this may take a while depending on dataset size)")
    feature_list = []
    
    for url in df['url']:
        # Ensure the URL is a string
        features = extract_features(str(url))
        feature_list.append(features)

    # 3. Create a new DataFrame for features
    column_names = [
        'url_len', 'domain_len', 'dot_count', 'hyphen_count', 
        'at_count', 'query_count', 'is_ip', 'is_https', 
        'subdomain_count', 'sensitive_word_count'
    ]
    
    feature_df = pd.DataFrame(feature_list, columns=column_names)

    # 4. Combine features with the original labels
    final_df = pd.concat([feature_df, df['label'].reset_index(drop=True)], axis=1)

    # 5. Save the processed data for training
    final_df.to_csv(output_file, index=False)
    print(f"--- Process Complete! Processed data saved to {output_file} ---")

if __name__ == "__main__":
    # Replace 'urldata.csv' with your actual downloaded filename
    collect_and_prepare_data('malicious_phish.csv', 'processed_data.csv')