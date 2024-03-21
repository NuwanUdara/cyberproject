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
  print("Key: ",key)

  # Create an AES cipher object with the generated key.
  ciper = AES.new(key, AES.MODE_CBC)

  # Enconde using the utf-8 character set and add the padding to the phrase.
  
  
  # Encrypt the phrase.
  

  # Encode the encrypted phrase to base64"
  
    
  # Return the output of encrypted phrase and the key.
  return encrypted_phrase, key


def pad(data, block_size):
  """ Function pads a string (Phrase entered by user) to a multiple of the specified block size to meet AES requirments.
  Inouts:
    data: The phrase to be pad.
    block_size: The block size to be pad to.
  Outpur:
    The padded string (Phrase).
  """

  padding_len =
  padding = 
  return data + padding


if __name__ == "__main__":
  # Get the phrase to encrypt from the user.
  phrase = input("Enter the phrase to encrypt: ")

  # Encrypt the phrase.


  # Print the encrypted phrase, passphrase, and the key.
