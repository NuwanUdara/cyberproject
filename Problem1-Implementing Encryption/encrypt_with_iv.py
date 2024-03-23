import os
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

def encrypt_phrase(phrase):
    """Function encrypts a phrase using AES key generated within the function.
    Inputs:
        phrase: The phrase to encrypt.
    Output:
        Encrypted phrase and the key used.
    """
    # Generate a 16-byte random key.
    key = os.urandom(16)

    # Generate a random IV
    iv = os.urandom(AES.block_size)

    # Create an AES cipher object with the generated key and IV.
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Pad the phrase to a multiple of the block size.
    padded_phrase = pad(phrase.encode('utf-8'), AES.block_size)

    # Encrypt the padded phrase.
    encrypted_phrase = cipher.encrypt(padded_phrase)

    # Combine the IV and the encrypted phrase.
    combined_data = iv + encrypted_phrase

    # Encode the combined data to base64.
    encrypted_phrase_str = base64.b64encode(combined_data).decode('utf-8')

    return encrypted_phrase_str, key, iv

if __name__ == "__main__":
    # Get the phrase to encrypt from the user.
    phrase = input("Enter the phrase to encrypt: ")

    # Encrypt the phrase.
    encrypted_phrase, key, iv = encrypt_phrase(phrase)

    # Print the encrypted phrase, passphrase, key, and IV.
    print("Encrypted phrase:", encrypted_phrase)
    print("Key:", key)
    print("IV:", iv)