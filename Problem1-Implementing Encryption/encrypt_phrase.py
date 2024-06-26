import os
import base64
import random
from Crypto.Cipher import AES

def encrypt_phrase(phrase):
  """Function encrypts a phrase using AES key generated within the function.
  Inputs:
    phrase: The phrase to encrypt.
  Output:
    Encrypted phrase and the key used.
  """

  # Generate a 16-byte random key.
  key = os.urandom(16)

  # Create an AES cipher object with the generated key.
  ciper = AES.new(key, AES.MODE_CBC)

  # Enconde using the utf-8 character set and add the padding to the phrase.
  phrase = phrase.encode('utf-8')
  phrase = pad(phrase, AES.block_size)

  # Encrypt the phrase.
  encrypted_phrase = ciper.encrypt(phrase)

  # Encode the encrypted phrase to base64"
  encrypted_phrase = base64.b64encode(encrypted_phrase)
  
    
  # Return the output of encrypted phrase and the key.
  return encrypted_phrase, key


def pad(data, block_size):
    """ Function pads a string (Phrase entered by user) to a multiple of the specified block size to meet AES requirements.
    Inputs:
        data: The phrase to be padded.
        block_size: The block size to be padded to.
    Output:
        The padded string (Phrase).
    """
    padding_len = block_size - (len(data) % block_size)
    padding = bytes([padding_len] * padding_len) # PKCS#7 padding technuique is used
    return data + padding

if __name__ == "__main__":
  # Get the phrase to encrypt from the user.
  phrase = input("Enter the phrase to encrypt: ")

  # Encrypt the phrase.
  output,key = encrypt_phrase(phrase)
  print("Before decode",output)
  encrypted_phrase_str = output.decode('utf-8')
  # Print the encrypted phrase, passphrase, and the key.
  print("Phase:", phrase, "Passphrase:", encrypted_phrase_str, "Key:", key)