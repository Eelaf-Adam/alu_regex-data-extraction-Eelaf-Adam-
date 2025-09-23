# 👋🏽 Welcome to Regex Data Extraction Tool 🔍

This tool will validate various data types using Regular Expressions (regex). It supports validating email addresses, URLs, phone numbers, currency amounts, and time. These tools does not only test the data against the regex provided it also allows the user to enter their own input for validation allowing in an interactive menu based.

## Setup Instructions ⚙️

First: Clone the repository on your local machine:
```
git clone https://github.com/Eelaf-Adam/alu_regex-data-extraction-Eelaf-Adam
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

## Director structure 📂
```
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

















