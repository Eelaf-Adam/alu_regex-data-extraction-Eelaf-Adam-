# 👋🏽 Welcome to Regex Data Extraction Tool 🔍

This tool will validate various data types using Regular Expressions (regex). It supports validating email addresses, URLs, phone numbers, currency amounts, and time. These tools does not only test the data against the regex provided it also allows the user to enter their own input for validation allowing in an interactive menu based.

## Setup Instructions ⚙️

First: Clone the repository on your local machine:
```
git clone https://github.com/Eelaf-Adam/alu_regex-data-extraction-Eelaf-Adam-.git
```

Second: Navigate to the cloned repository:
```
cd alu_regex-data-extraction-Eelaf-Adam
```

Third: Run the main script:
```
python3 main.py
```

## Usage 🔐
1. After running the script choose from the menu:
  - Validate sample email addresses
  - validate sample URLs
  - Validate sample phone numbers
  - Validate sample currency amounts
  - Validate sample times
  - Test your own input against any validator
    
2. For sample tests, the tool will automatically validate all built-in test data.

3. For custom input, simply enter your own string when prompted.

4. Exit the tool anytime by selecting option 7.

# Sample OutPut 📤

1. Email 
```sh
Choose an option (1-7): 1

--- Testing Sample Data ---
user@example.com Valid Email
firstname.lastname@company.co.uk Valid Email
user.name+tag+sorting@example.com Valid Email
user_name@sub.company.com Valid Email
user@123.123.123.123 Invalid Email
user@localhost Invalid Email
user@.com Invalid Email
user@com Invalid Email
```

2. URLs
```sh
Choose an option (1-7): 2

--- Testing Sample Data ---
https://www.example.comLinks to an external site. Invalid URL
https://subdomain.example.org/pageLinks to an external site. Invalid URL
http://localhost Valid URL
https://192.168.1.1/path Valid URL
https://www.example.com?query=test Invalid URL
https://www.example.com#anchor Invalid URL
ftp://example.com Invalid URL
http://invalid-url.com Valid URL
```

3. Phone numbers
```sh
Choose an option (1-7): 3

--- Testing Sample Data ---
(123) 456-7890 Valid Phone Number
123-456-7890 Valid Phone Number
123.456.7890 Valid Phone Number
123 456 7890 Valid Phone Number
+1 123-456-7890 Valid Phone Number
1123-456-7890 Invalid Phone Number
1234567890 Valid Phone Number
```

4. Currency 
```sh
Choose an option (1-7): 4

--- Testing Sample Data ---
$19.99 Valid Currency
$1,234.56 Valid Currency
$1234 Invalid Currency
$12.3 Invalid Currency
$0.99 Valid Currency
£2,500.00 Invalid Currency
1200 Invalid Currency
```

5. Time 
``sh
Choose an option (1-7): 5

--- Testing Sample Data ---
14:30 Valid Time
2:30 PM Valid Time
02:05 am Valid Time
00:00 Valid Time
12:00 PM Valid Time
23:59 Valid Time
13:60 Invalid Time
```

## Director structure 📂
```sh
regex-data-validation-tool-Eelaf-Adam/
├── README.md              # Project documentation
├── main.py                # Main program entry point
├── validators/            # Folder containing validators
│   ├── email_validator.py
│   ├── urls_validator.py
│   ├── phone_validator.py
│   ├── currency_validator.py
│   ├── time_validator.py

```
## Features & Programming Concepts 💡

### Validation with Regex:  
Covers multiple formats and edge cases for emails, URLs, phone numbers, times, and currencies.

### Interactive CLI Menu:
Navigate through validators or test custom inputs.

### Error Handling: 
Handles invalid or empty input gracefully.

### Modular Design: 
Each validator is in its own Python file for clarity and reusability.

### Lightweight: 
Uses only Python’s built-in re and sys modules.

# Contact Information 🌟
👩🏽‍💻[**Eelaf Adam**](https://github.com/Eelaf-Adam)
📧[**Email**](e.adam@alustudent.com)

# License 📑
Copyright © 2025
This project is licensed under the MIT License



















