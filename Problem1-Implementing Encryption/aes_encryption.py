import os
import base64
from cryptography.fernet import Fernet

def encrypt_phrase(phrase):
  
  # Generate a random key.
  key = Fernet.generate_key()
  print("Base64 Encoded Key:", key)
  print("Length:",len(key))

  # # try:
  #   base64decoded_key = base64.b64decode(key)
  #   print("Decoded true Key:",base64decoded_key)
  #   print("Length:" ,len(base64decoded_key))
  # # except:
  #   print("Decoded key is not base64 encoded")

  try:
        # Decode the base64 encoded key.
        decoded_key = base64.urlsafe_b64decode(key)
        print("Decoded Key:", decoded_key)
        print("Length:", len(decoded_key))
  except Exception as e:
        print("Error:", e)
        #even with this error the encrytion will carry out fine

  # Create a Fernet object with the key.
  f = Fernet(key)
  
  # Encrypt the phrase, while enconding using the utf-8 character set. 
  encrypted_phrase = f.encrypt(phrase.encode('utf-8'))
  # Return the encrypted phrase and key.
  return encrypted_phrase, key


if __name__ == "__main__":

  # Get the phrase to encrypt from the user.
  phrase = input("Enter the phrase to encrypt: ")

  # Encrypt the phrase, calling the encryption function.
  encrypted_phrase, key = encrypt_phrase(phrase)

  # Print the encrypted phrase and key
  print("Encrypted phrase:", encrypted_phrase)
  print("Key:", key)

  #save key and encrypted phrase in files
  with open('key.txt', 'a') as f:
    # f.write(str(key))
    f.writelines('\n'+str(key))
    
  
  with open('encrypted_phrase.txt', 'a') as f:
    # f.write(str(encrypted_phrase))
    f.writelines('\n'+str(key))
