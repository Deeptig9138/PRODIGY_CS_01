def encrypt(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_message += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_message += char
    return encrypted_message

def decrypt(message, shift):
    return encrypt(message, -shift)

def main():
    print("Caesar Cipher Program")
    while True:
        choice = input("Do you want to (e)ncrypt or (d)ecrypt a message? (e/d) or 'q' to quit: ").lower()
        if choice == 'q':
            print("Goodbye!")
            break
        elif choice in ['e', 'd']:
            message = input("Enter the message: ")
            try:
                shift = int(input("Enter the shift value (e.g., 3): "))
            except ValueError:
                print("Invalid shift value. Please enter a valid integer.")
                continue
            if choice == 'e':
                result = encrypt(message, shift)
            else:
                result = decrypt(message, shift)
            print(f"Result: {result}\n")
        else:
            print("Invalid choice. Please enter 'e', 'd', or 'q'.")

if __name__ == "__main__":
    main()
