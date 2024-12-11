import random
import string

def generate_password(length, use_uppercase=True, use_numbers=True, use_special_chars=True):
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if use_uppercase else ''
    numbers = string.digits if use_numbers else ''
    special_chars = string.punctuation if use_special_chars else ''
    
    # Combine selected character sets
    all_chars = lowercase + uppercase + numbers + special_chars
    
    if not all_chars:
        raise ValueError("At least one character type must be selected.")
    if length < 1:
        raise ValueError("Password length must be at least 1.")
    
    # Generate password
    password = ''.join(random.choices(all_chars, k=length))
    return password

def main():
    print("Welcome to the Password Generator!")
    
    try:
        # Get user preferences
        length = int(input("Enter the desired password length: "))
        use_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
        use_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
        use_special_chars = input("Include special characters? (y/n): ").strip().lower() == 'y'
        
        # Generate and display the password
        password = generate_password(length, use_uppercase, use_numbers, use_special_chars)
        print("\nGenerated Password:", password)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()