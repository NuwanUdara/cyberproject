from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import Crypto
import os

def encrypt_file(input_file_path, public_key_path, output_file_path):
    # Use the proper read write formats where necessary (its missing in the code)
    # Read the file content
    with open(input_file_path,) as file:
        data = file.read()
    
    print("Data", data)
    print("length", len(data))
    # Read the private key
    with open(public_key_path,) as key_file:
        public_key = RSA.import_key(key_file.read())

    # Encrypt the data with RSA
    cipher_rsa = PKCS1_OAEP.new(public_key,hashAlgo=Crypto.Hash.SHA256)
    # encrypted_data = cipher_rsa.encrypt(data)
    encrypted_data = cipher_rsa.encrypt(data.encode('utf-8'))

    # Write the encrypted data to the output file
    with open(output_file_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)

    print(f'Encryption complete. Encrypted file saved to: {output_file_path}')

if __name__ == "__main__":
    # Get user input
    # Use .strip() function to remove any whitespaces from the begining and/or end of input value
    input_file_path = input("Enter the path to the input file: ").strip()
    public_key_path = input("Enter the path to the Public key file (.pem): ").strip()
    output_file_path = input("Enter the output path for the encrypted file: ").strip()

    # Check for the existence of both files
    if not (os.path.isfile(input_file_path) and os.path.isfile(public_key_path)):
        print("Error: Input file or Public key file not found.")
    else:
        encrypt_file(input_file_path, public_key_path, output_file_path)
