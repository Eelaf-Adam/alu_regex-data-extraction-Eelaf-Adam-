import re 

# Provided sample emails 
sample_data = [
    "user@example.com",
    "firstname.lastname@company.co.uk"
]

pattern = r'^[\w\.-]+@[\w\.-]+\w+$'

"""
Regex Explanation: 

"""

def validate(test_string):
    """ Validate a single email string. """
    if re.match(pattern, test_string):
        print(f"{test_string} Valid Email")

    else:
        print(f"{test_string} Invalid Email")


def run_sample_data():
    """ Run validation on all sample data. """
    print("\n--- Email Validator Sample Tests ---")
    for s in sample_data:
        validate(s)

