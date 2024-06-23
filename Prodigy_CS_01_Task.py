def encrypt_caesar_cipher(plain_text, shift):
    encrypted_text = ""
    for char in plain_text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt_caesar_cipher(cipher_text, shift):
    return encrypt_caesar_cipher(cipher_text, -shift)

def main():
    while True:
        print("Caesar Cipher Encryption/Decryption")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            message = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value: "))
            encrypted_message = encrypt_caesar_cipher(message, shift)
            print(f"Encrypted Message: {encrypted_message}\n")
        
        elif choice == '2':
            message = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift value: "))
            decrypted_message = decrypt_caesar_cipher(message, shift)
            print(f"Decrypted Message: {decrypted_message}\n")
        
        elif choice == '3':
            print("Exiting...")
            break
        
        else:
            print("Invalid option, please choose again.")

if __name__ == "__main__":
    main()
