import sys 
from validators import (
    email_validator,
    urls_validator,
    phone_validator,
    currency_validator,
    time_validator
)

def data_extraxtion_menu():
    print("\n=== Regex Data Extractin App ===")
    print("1. Validate Email Adress")
    print("2. Validate URL")
    print("3. Validate Phone Number")
    print("4. Validate Currency Amount")
    print("5. Validate Time")
    print("6. Exit")


def run_validator(choice):
    test_string  = input("Enter a string to validate:")

    if choice == "1":
        email_validator.validate(test_string)
    elif choice == "2":
        urls_validator.validate(test_string)
    elif choice == "3":
        phone_validator.validate(test_string)
    elif choice == "4":
        currency_validator.validate(test_string)
    elif choice == "5":
        time_validator.validate(test_string)
    else:
        print("Invalid Option. ")

    
if __name__ == "__main__":
    while True:
        data_extraxtion_menu()
        choice = input("Choose an option (1-6): ").strip()
        if choice == "6":
            print("Thank You For Using The Regex Data Extraxtion App ")
            sys.exit(0)
        else:
            run_validator(choice)
        
