import sys 
from validators import (
    email_validator,
    urls_validator,
    phone_validator,
    currency_validator,
    time_validator
)

def data_extraxtion_menu():
    print("\n=== Regex Data Extractin Tool ===")
    print("1. Validate Sample Email Adress")
    print("2. Validate Sample URLs")
    print("3. Validate  Sample Phone Number")
    print("4. Validate  Sample Currency Amount")
    print("5. Validate  Sample Time")
    print("6. Test Your Own Input")
    print("7. Exit")


def run_validator(choice, test_string=None):
    """Run validator for either sample data or user input data."""
    
    validators_map = {
    "1": email_validator,
    "2": urls_validator,
    "3": phone_validator,
    "4": currency_validator,
    "5": time_validator
}
    
    validator = validators_map.get(choice)
    if not validator:
        print(" Invalid option. Please choose a number between 1-5.")
        return
    

    try:
        # User provided input
        if test_string is not None:
            if not test_string.strip():
                (" Empty input provided. Please enter a valid string.")
                return
            validator.validate(test_string)
            return
        
        # Test predefined sample data from validator module
        print("\n--- Testing Sample Data ---")
        for sample in getattr(validator, "sample_data", []):
            validator.validate(sample)

    except Exception as e:
        print(f" An error occurred during validation: {e}")

def get_valid_sub_choice():
    """Prompt the user untill they enter a valid choice (1-5)."""
    while True:
        sub_choice = input("Choose a validator (1-5)").strip()
        if not sub_choice:
            print(" No input entered. Please enter a number between 1-5.")
            continue
        if sub_choice not in ["1", "2", "3", "4", "5"]:
            print("Invalid choice. Please enter a number between 1-5.")
            continue
        return sub_choice
    
    
if __name__ == "__main__":
    while True:
        try:
            data_extraxtion_menu()
            choice = input("Choose an option (1-7): ").strip()

            if choice == "7":
                print("Thank You For Using The Regex Data Extraxtion Tool ")
                sys.exit(0)

            elif choice == "6":
                print("\n--- Test Your Own Input ---")
                print("1. Email\n2. URL\n3. Phone\n4. Currency\n5. Time")
                sub_choice = input("Choose a validator (1-5:) ").strip()
                while True:
                    user_input = input("Enter a string to validate: ").strip()
                    if user_input:
                        break
                    print("Empty input provided enter a valid string. ")
                run_validator(sub_choice, user_input)

            elif choice in ["1", "2", "3", "4", "5"]:
                run_validator(choice)

            else:
                print(" Invalid option, please choose a number between 1-7.")

        except KeyboardInterrupt:
            print("\n\nExiting... Thank You!")
            sys.exit(0)
        except Exception as e:
            print(f" Unexpected error: {e}")

        
        
