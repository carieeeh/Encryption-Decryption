#Encryption and Decryption of txt file

def encrypt_file(input_file, output_file, key):
    try:
        with open(input_file, 'r') as file:
            plaintext = file.read()

        ciphertext = ""
        for char in plaintext:
            if char.isalpha():
                ascii_offset = ord('A') if char.isupper() else ord('a')
                shifted = (ord(char) - ascii_offset + key) % 26 + ascii_offset
                ciphertext += chr(shifted)
            else:
                ciphertext += char

        with open(output_file, 'w') as file:
            file.write(ciphertext)

        print("File encrypted successfully.\n")

    except IOError as e:
        print("Error: Unable to encrypt file. ", str(e))

def decrypt_file(input_file, output_file, key):
    try:
        with open(input_file, 'r') as file:
            ciphertext = file.read()

        plaintext = ""
        for char in ciphertext:
            if char.isalpha():
                ascii_offset = ord('A') if char.isupper() else ord('a')
                shifted = (ord(char) - ascii_offset - key) % 26 + ascii_offset
                plaintext += chr(shifted)
            else:
                plaintext += char

        with open(output_file, 'w') as file:
            file.write(plaintext)

        print("File decrypted successfully.\n")

    except IOError as e:
        print("Error: Unable to decrypt file. ", str(e))

# Main program
def main():
    while True:
        print("=== File Encryption/Decryption ===")
        print("1. Encrypt a file")
        print("2. Decrypt a file")
        print("3. Exit")
        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':  # Encrypt a file
            file_path = input("Enter the path of the file to encrypt: ")
            output_file = input("Enter the path for the encrypted output file: ")
            key = int(input("Enter the encryption key (an integer): "))
            encrypt_file(file_path, output_file, key)
            print("File encrypted successfully.\n")
        elif choice == '2':  # Decrypt a file
            file_path = input("Enter the path of the file to decrypt: ")
            output_file = input("Enter the path for the decrypted output file: ")
            key = int(input("Enter the decryption key (an integer): "))
            decrypt_file(file_path, output_file, key)
            print("File decrypted successfully.\n")
        elif choice == '3':  # Exit the program
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.\n")

if __name__ == "__main__":
    main()