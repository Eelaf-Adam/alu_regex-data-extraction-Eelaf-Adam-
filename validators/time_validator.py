import re 

sample_data = [
    "14:30",
    "2:30 PM",
]

pattern = r'^(?:[01]\d|2[0-3]):[0-5]\d|([1-9]|1[0-2]):[0-5]\d\s?(AM|PM))$'

"""
Regex Explaniation:

"""

def validate(test_string):
    """ Validate a simple time string. """
    if re.match(pattern, test_string, re.IGNORECASE):
        print(f"{test_string} Valid Time")
    else:
        print(f"{test_string} Invalid Time")


def run_sample_date():
    """ Run valiation on all sample time data. """
    print("\n--- Time Validator Sample Test ---")
    for s in sample_data:
        validate(s)