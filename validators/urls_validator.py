import re 

sample_data = [
    "https://www.example.comLinks to an external site."
    "https://subdomain.example.org/pageLinks to an external site."
]

pattern = r'^https?:\/\/[^\s\/$.?#].[^\s]*$'

"""
Reges Explaniation:

"""

def validate(test_string):
    """ Validate a single URL string."""
    if re.match(pattern, test_string):
        print(f"{test_string} Valid URL")
    else:
        print(f"{test_string} Invalid URL")


def run_sample_data():
    """ Run validation on all sample URL data. """
    print("\n--- URL Validator Sample Tests ---")
    for s in sample_data:
        validate(s)