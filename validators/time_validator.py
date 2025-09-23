import re 

sample_data = [
    "14:30", # 24 hour
    "2:30 PM", # 12 hour
    "02:05 am", # Lowercase AM/PM
    "00:00", # Midnight 24 hour
    "12:00 PM", # Noon 12 hour
    "23:59", # Edge case 24 hour max 
    "13:60", # Invalid minute (for negative testing)
]

pattern = r'^((([01]?\d|2[0-3]):[0-5]\d)|((1[0-2]|0?[1-9]):[0-5]\d\s?([AaPp][Mm])))$'

"""
Regex Explaniation:
Supports 24 hour times from 00:00 t0 23:59, support 12 hour format with AM/PM case insensetive, and covers edge cases like midnight, noon, and invalid minutes for testing.
"""

def validate(test_string):
    """ Validate a simple time string. """
    if re.fullmatch(pattern, test_string, re.IGNORECASE):
        print(f"{test_string} Valid Time")
    else:
        print(f"{test_string} Invalid Time")


def run_sample_date():
    """ Run valiation on all sample time data. """
    print("\n--- Time Validator Sample Test ---")
    for s in sample_data:
        validate(s)