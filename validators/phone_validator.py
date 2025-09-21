import re 

sample_data = [
   "(123) 456-7890",
   "123-456-7890",
   "123.456.7890"
]


pattern = r'^(\(\d{3}\)\s||d{3}[-.])\d{3}[-.]\d{4}$'

""" 
Regex Eplanation:

"""

def validate(test_string):
    if re.match(pattern, test_string):
        print(f"{test_string} Valid Phone Number")
    else:
        print(f"{test_string} Invalid Phone Number")


def run_sample_date():
    print("\n--- Phone Validator Sample Tests ---")
    for s in sample_data:
        validate(s)