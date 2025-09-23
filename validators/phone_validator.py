import re 

sample_data = [
   "(123) 456-7890",
   "123-456-7890",
   "123.456.7890",
   "123 456 7890",
   "+1 123-456-7890",
   "1123-456-7890",
   "1234567890"  # Edge case: no delimiters
]


pattern = r'^(?:\+1\s?)?(?:\(\d{3}\)|\d{3})[\s.-]?\d{3}[\s.-]?\d{4}$'

""" 
Regex Eplanation:
It validates common U.S. phone number formats, with or without country code using spaces, dots, dashes, or parentheses for separators. 
"""

def validate(test_string):
    if re.fullmatch(pattern, test_string):
        print(f"{test_string} Valid Phone Number")
    else:
        print(f"{test_string} Invalid Phone Number")


def run_sample_date():
    print("\n--- Phone Validator Sample Tests ---")
    for s in sample_data:
        validate(s)