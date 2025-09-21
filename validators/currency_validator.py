import re 

sample_data = [
    "$19.99",
    "$1,234.56"
]

pattern = r'^\$\d{1,3}(,\d{3})*(\.\d{2})?$'

"""
Reges Explaniation:

"""

def validate(test_string):
    """ Validate a single currency string. """
    if re.match(pattern, test_string):
        print(f"{test_string} Valid Currency")
    else:
        print(f"{test_string} Invalid Currency")


def run_sample_data():
    """ Run validation on all sample currency data. """
    print("\n--- Currency Validator Sample Tests ---")
    for s in sample_data:
        validate(s)
