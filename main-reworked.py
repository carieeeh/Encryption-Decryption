# Encryption and decryption of txt file
# BSIT-3A-M Group Project

# Submitted by:
# Cabrera, Jacob Emmanuel
# Malinay, John Loyd
# Moises, Eisen Lois
# Velasquez, Loven Joy
# Villadelgado, Janne Carol


# Encryption Function
def encrypt_file(input_file, output_file, key):
    try:
        # Read the input file
        with open(input_file, 'r', encoding='utf-8') as file:
            plaintext = file.read()

        ciphertext = ""  # Initialization to store encrypted text
        for i, char in enumerate(plaintext):
            key_char = key[i % len(key)]  # Repeat key characters if necessary
            encrypted_char = chr(ord(char) + ord(key_char))  # Shift the character by the corresponding key character
            ciphertext += encrypted_char

        # Write the encrypted text to the output file
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(ciphertext)

        print("File encrypted successfully.\n")

    except FileNotFoundError:
        print("Error: Input file not found.")
    except IOError as e:
        print("Error: Unable to encrypt file. ", str(e))


# Decryption Function
def decrypt_file(input_file, output_file, key):
    try:
        # Read the input file
        with open(input_file, 'r', encoding='utf-8') as file:
            ciphertext = file.read()

        plaintext = ""
        for i, char in enumerate(ciphertext):
            key_char = key[i % len(key)]  # Repeat key characters if necessary
            decrypted_char = chr(ord(char) - ord(key_char))  # Shift the character back by the corresponding key character
            plaintext += decrypted_char

        # Write the decrypted text to the output file
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(plaintext)

        print("File decrypted successfully.\n")

    except FileNotFoundError:
        print("Error: Input file not found.")
    except IOError as e:
        print("Error: Unable to decrypt file. ", str(e))


# Main program
def main():
    while True:
        print("=== File Encryption/Decryption ===")
        print("[1] Encrypt a file")
        print("[2] Decrypt a file")
        print("[3] Exit")
        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':  # Encrypt a file
            file_path = input("Enter the path of the file to encrypt: ")
            output_file = input("Enter the path for the encrypted output file: ")
            key = input("Enter the encryption key (a string of letters and/or numbers): ")
            encrypt_file(file_path, output_file, key)
        elif choice == '2':  # Decrypt a file
            file_path = input("Enter the path of the file to decrypt: ")
            output_file = input("Enter the path for the decrypted output file: ")
            key = input("Enter the decryption key (a string of letters and/or numbers): ")
            decrypt_file(file_path, output_file, key)
        elif choice == '3':  # Exit the program
            print("Exiting the program.")
            break
        else:
            print("Invalid choice! Please select 1, 2, or 3 only.\n")


if __name__ == "__main__":
    main()
