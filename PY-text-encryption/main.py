# install 'cryptography'
from cryptography.fernet import Fernet
import base64
import hashlib

# Function to generate a key from the password
def generate_key(password):
    # Use SHA-256 to hash the password
    hashed_password = hashlib.sha256(password.encode()).digest()
    # Use the first 32 bytes of the hashed password to create the key
    key = base64.urlsafe_b64encode(hashed_password[:32])
    return key

# Encrypt the message
def encrypt_message(message, password):
    key = generate_key(password)
    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(message.encode())
    return encrypted_message.decode("utf-8") # to return as the normal str obj

# Decrypt the message
def decrypt_message(encrypted_message, password):
    key = generate_key(password)
    fernet = Fernet(key)
    decrypted_message = fernet.decrypt(encrypted_message).decode()
    return decrypted_message


if __name__ == "__main__":
    # Sample usage
    message = "hello geeks"
    password = "mypassword"

    # Encrypt the message
    encrypted_message = encrypt_message(message, password)
    print("Encrypted:", encrypted_message)
    print("type: ", type(encrypted_message))

    # Decrypt the message
    decrypted_message = decrypt_message(encrypted_message, password)
    print("Decrypted:", decrypted_message)
    print("type: ", type(decrypted_message))