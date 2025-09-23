import re 

# Provided sample emails 
sample_data = [
    "user@example.com",
    "firstname.lastname@company.co.uk",
    "user.name+tag+sorting@example.com", # Edge case with +
    "user_name@sub.company.com", # Subdomain
    "user@123.123.123.123",  # IP as domain
    "user@localhost",  # Local domain (invalid in most cases)
    "user@.com", # Invalid
    "user@com"   # Invalid
]

pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

"""
Regex Explanation: 
This validates standard email formats with a local part, and '@' symbol, a domain name, and a valid domain suffix (e.g., .com, .org, .co.uk).
"""

def validate(test_string):
    """ Validate a single email string. """
    if re.fullmatch(pattern, test_string):
        print(f"{test_string} Valid Email")

    else:
        print(f"{test_string} Invalid Email")

def run_sample_data():
    """ Run validation on all sample data. """
    print("\n--- Email Validator Sample Tests ---")
    for s in sample_data:
        validate(s)

