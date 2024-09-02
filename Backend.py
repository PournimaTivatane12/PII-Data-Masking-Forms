from flask import Flask, request, jsonify
import re

app = Flask(__name__)

# Function to mask PII data
def mask_pii(data):
    # Mask email addresses
    email_pattern = re.compile(r'([a-zA-Z0-9_.+-]+)@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
    data = email_pattern.sub(lambda x: mask_email(x.group()), data)

    # Mask credit card numbers (example format: 1234-5678-9876-5432)
    cc_pattern = re.compile(r'\b(?:\d[ -]*?){13,16}\b')
    data = cc_pattern.sub(lambda x: mask_credit_card(x.group()), data)

    # Mask Social Security Numbers (example format: 123-45-6789)
    ssn_pattern = re.compile(r'\b\d{3}-\d{2}-\d{4}\b')
    data = ssn_pattern.sub(lambda x: mask_ssn(x.group()), data)

    return data

# Function to mask email by keeping first and last letters visible
def mask_email(email):
    name, domain = email.split('@')
    masked_name = name[0] + '*' * (len(name) - 2) + name[-1]
    return masked_name + '@' + domain

# Function to mask credit card numbers, keeping the last 4 digits visible
def mask_credit_card(cc_number):
    return '*' * (len(cc_number) - 4) + cc_number[-4:]

# Function to mask SSN, keeping the last 4 digits visible
def mask_ssn(ssn):
    return '***-**-' + ssn[-4:]

# API endpoint to accept form data
@app.route('/mask', methods=['POST'])
def mask_form_data():
    data = request.get_json()
    if not data or 'form_data' not in data:
        return jsonify({"error": "Invalid input"}), 400

    form_data = data['form_data']
    masked_data = mask_pii(form_data)

    return jsonify({"masked_data": masked_data})

if __name__ == '__main__':
    app.run(debug=True)
