import re
import tldextract
from urllib.parse import urlparse

def extract_features(url):
    features = []
    
    # 1. Parsing the URL components
    parsed_url = urlparse(url)
    extracted = tldextract.extract(url)
    domain = extracted.domain
    
    # 2. Length-based features
    features.append(len(url))               # Total URL Length
    features.append(len(domain))            # Length of the domain name
    
    # 3. Special Character Counts (Phishing sites often use these to mimic brands)
    features.append(url.count('.'))         # Number of dots
    features.append(url.count('-'))         # Number of hyphens
    features.append(url.count('@'))         # Presence of @ (ignores everything before it)
    features.append(url.count('?'))         # Query parameters
    
    # 4. Digital fingerprinting
    # Check if the domain is an IP address instead of a name
    is_ip = 1 if re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", domain) else 0
    features.append(is_ip)
    
    # 5. Protocol Analysis
    # Most modern phishing uses HTTPS now, but it's still a standard feature
    features.append(1 if parsed_url.scheme == 'https' else 0)
    
    # 6. Subdomain count
    # Example: 'paypal.secure-login.com' has more subdomains than 'paypal.com'
    subdomains = extracted.subdomain.split('.')
    features.append(len(subdomains) if subdomains[0] != '' else 0)

    # 7. Presence of "Sensitive" words in the URL
    sensitive_words = ['login', 'verify', 'bank', 'secure', 'update', 'signin', 'account']
    found_word = 0
    for word in sensitive_words:
        if word in url.lower():
            found_word = 1
            break
    features.append(found_word)

    return features

# --- Test the script ---
test_url = "http://secure-login-paypal-verify.com/update"
features_output = extract_features(test_url)
print(f"Features for {test_url}: \n{features_output}")