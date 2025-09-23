import re 

sample_data = [
    "https://www.example.comLinks to an external site.",
    "https://subdomain.example.org/pageLinks to an external site.",
    "http://localhost", # Edge localhost URL
    "https://192.168.1.1/path", # IP address URL
    "https://www.example.com?query=test", # URL with query
    "https://www.example.com#anchor", # URL with anchor
    "ftp://example.com", # Invalid 9only http/https valid)
    "http://invalid-url.com" # Invalid (space)

]

pattern = r'^(https?):\/\/(([A-Za-z0-9-]+\.)+[A-Za-z]{2,}|localhost|(\d{1,3}\.){3}\d{1,3})(:\d+)?(\/\S*)?$'

"""
Reges Explaniation:
Allow http/https only with domain names, localhost, or IPs to handle ports, paths, queries, and anchors disallow inavalid spaces.
"""

def validate(test_string):
    """ Validate a single URL string."""
    if re.fullmatch(pattern, test_string):
        print(f"{test_string} Valid URL")
    else:
        print(f"{test_string} Invalid URL")


def run_sample_data():
    """ Run validation on all sample URL data. """
    print("\n--- URL Validator Sample Tests ---")
    for s in sample_data:
        validate(s)