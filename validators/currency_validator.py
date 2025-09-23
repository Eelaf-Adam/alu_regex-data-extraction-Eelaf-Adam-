import re 

sample_data = [
    "$19.99",  # US Dollar 
    "$1,234.56", # US Dollar with comma
    "$1234",     # US Dollar, no comma
    "$12.3",     # US Dollar, single decimal
    "$0.99",     # US Dollar, less than 1
    "£2,500.00", # Brithish Pound (invalid)
    "1200"      # No specfici currency (edge case)
]

pattern = r'^\$\d{1,3}(,\d{3})*(\.\d{2})?$'

"""
Reges Explaniation:
It validates the standard U.S currency formats that begins with a dollar sign and may include commas and cents. 
"""

def validate(test_string):
    """ Validate a single currency string. """
    if re.fullmatch(pattern, test_string):
        print(f"{test_string} Valid Currency")
    else:
        print(f"{test_string} Invalid Currency")



def run_sample_data():
    """ Run validation on all sample currency data. """
    print("\n--- Currency Validator Sample Tests ---")
    for s in sample_data:
        validate(s)
