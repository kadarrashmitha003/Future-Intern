import random
import string

def generate_password(length, include_uppercase, include_numbers, include_special):
    """Generates a random password based on the given criteria."""
    # Define character sets
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase if include_uppercase else ''
    numbers = string.digits if include_numbers else ''
    special_characters = string.punctuation if include_special else ''
    
    # Combine all selected character sets
    all_characters = lowercase_letters + uppercase_letters + numbers + special_characters

    if not all_characters:
        raise ValueError("At least one type of character must be selected.")
    
    # Generate password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

def main():
    """Main function to interact with the user and generate the password."""
    print("Welcome to the Random Password Generator!")
    
    # Get user input
    try:
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            raise ValueError("Password length must be a positive integer.")
        
        include_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == 'yes'
        include_numbers = input("Include numbers? (yes/no): ").strip().lower() == 'yes'
        include_special = input("Include special characters? (yes/no): ").strip().lower() == 'yes'
        
        # Generate and display the password
        password = generate_password(length, include_uppercase, include_numbers, include_special)
        print(f"Generated Password: {password}")
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
