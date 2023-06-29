# Encryption and decryption of txt file
# BSIT-3A-M Group Project

# Submitted by: 
# Cabrera, Jacob Emmanuel
# Malinay, John Loyd
# Moises, Eisen Lois
# Velasquez, Loven Joy
# Villadelgado, Janne Carol


#Encryption Function
def encrypt_file(input_file, output_file, key):
    try:
        # Read the input file
        with open(input_file, 'r') as file:
            plaintext = file.read()

        ciphertext = "" #initialization to store encrypted text
        for char in plaintext:
            if char.isalpha(): # a method to check if the character is alphabet
                # Encrypt alphabetic characters
                ascii_offset = ord('A') if char.isupper() else ord('a') # ord function to obtain the ASCII value
                shifted = (ord(char) - ascii_offset + key) % 26 + ascii_offset
                ciphertext += chr(shifted)
            else:
                # Preserve non-alphabetic characters
                ciphertext += char

        # Write the encrypted text to the output file
        with open(output_file, 'w') as file:
            file.write(ciphertext)

        print("File encrypted successfully.\n")

    except FileNotFoundError:
        print("Error: Input file not found.")
    except IOError as e:
        print("Error: Unable to encrypt file. ", str(e))

#Decryption Function
def decrypt_file(input_file, output_file, key):
    try:
        # Read the input file
        with open(input_file, 'r') as file:
            ciphertext = file.read()

        plaintext = ""
        for char in ciphertext:
            if char.isalpha():
                # Decrypt alphabetic characters
                ascii_offset = ord('A') if char.isupper() else ord('a')
                shifted = (ord(char) - ascii_offset - key) % 26 + ascii_offset
                plaintext += chr(shifted)
            else:
                # Preserve non-alphabetic characters
                plaintext += char

        # Write the decrypted text to the output file
        with open(output_file, 'w') as file:
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
            key = int(input("Enter the encryption key (an integer): ")) 
            encrypt_file(file_path, output_file, key)
        elif choice == '2':  # Decrypt a file
            file_path = input("Enter the path of the file to decrypt: ")
            output_file = input("Enter the path for the decrypted output file: ")
            key = int(input("Enter the decryption key (an integer): ")) #Use a key that matches your encrypted key if you want to decrypt that file back
            decrypt_file(file_path, output_file, key)
        elif choice == '3':  # Exit the program
            print("Exiting the program.")
            break
        else:
            print("Invalid choice! Please select 1, 2, or 3 only.\n")

if __name__ == "__main__":
    main()
