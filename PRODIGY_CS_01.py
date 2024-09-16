# Caesar Cipher Encryption and Decryption

# Function to encrypt the text using the Caesar Cipher
def encrypt(text, shift):
    encrypted_text = ""
    
    for char in text:
        # Check if the character is an uppercase letter
        if char.isupper():
            # Find the position in the alphabet (0-25), apply the shift, and wrap around using modulo
            encrypted_text += chr((ord(char) + shift - 65) % 26 + 65)
        # Check if the character is a lowercase letter
        elif char.islower():
            # Apply the shift similarly for lowercase letters
            encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            # Non-alphabetical characters are not changed
            encrypted_text += char
    
    return encrypted_text

# Function to decrypt the text using the Caesar Cipher
def decrypt(text, shift):
    decrypted_text = ""
    
    for char in text:
        # Check if the character is an uppercase letter
        if char.isupper():
            # Reverse the shift for uppercase letters
            decrypted_text += chr((ord(char) - shift - 65) % 26 + 65)
        # Check if the character is a lowercase letter
        elif char.islower():
            # Reverse the shift for lowercase letters
            decrypted_text += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            # Non-alphabetical characters are not changed
            decrypted_text += char
    
    return decrypted_text

# Main function to interact with the user
def main():
    print("Caesar Cipher Program")
    
    # Get the choice from the user: encrypt or decrypt
    choice = input("Would you like to encrypt or decrypt a message? (e/d): ").lower()
    
    if choice not in ['e', 'd']:
        print("Invalid choice. Please select 'e' for encryption or 'd' for decryption.")
        return
    
    # Get the message and shift value from the user
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value (1-25): "))
    
    # Ensure the shift is within the range
    if shift < 1 or shift > 25:
        print("Invalid shift value. It must be between 1 and 25.")
        return
    
    # Perform encryption or decryption based on user choice
    if choice == 'e':
        result = encrypt(message, shift)
        print(f"Encrypted message: {result}")
    elif choice == 'd':
        result = decrypt(message, shift)
        print(f"Decrypted message: {result}")

# Run the program
if __name__ == "__main__":
    main()