def caesar_cipher(message, shift, mode):
    if mode == 'decrypt':
        shift = -shift
    result = ""
    for char in message:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char
    return result

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
                result = caesar_cipher(message, shift, 'encrypt')
            else:
                result = caesar_cipher(message, shift, 'decrypt')
            print(f"Result: {result}\n")
        else:
            print("Invalid choice. Please enter 'e', 'd', or 'q'.")

if __name__ == "__main__":
    main()
