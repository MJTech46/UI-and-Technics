# install 'pycryptodome'
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import scrypt
from Crypto.Random import get_random_bytes
import base64

def encrypt_message(message, password):
    # Generate a random salt
    salt = get_random_bytes(16)
    
    # Derive a key using the password and salt
    key = scrypt(password.encode(), salt, 32, N=2**14, r=8, p=1)
    
    # Generate a random initialization vector
    iv = get_random_bytes(16)
    
    # Create AES cipher
    cipher = AES.new(key, AES.MODE_GCM, iv)
    
    # Encrypt the message
    encrypted_message, tag = cipher.encrypt_and_digest(message.encode())
    
    # Encode the salt, iv, tag, and encrypted message in base64 for readability
    encrypted_message = base64.b64encode(salt + iv + tag + encrypted_message).decode()
    
    return encrypted_message

def decrypt_message(encrypted_message, password):
    # Decode the base64 encoded message
    encrypted_message = base64.b64decode(encrypted_message)
    
    # Extract the salt, iv, tag, and encrypted message
    salt = encrypted_message[:16]
    iv = encrypted_message[16:32]
    tag = encrypted_message[32:48]
    encrypted_message = encrypted_message[48:]
    
    # Derive the key using the password and salt
    key = scrypt(password.encode(), salt, 32, N=2**14, r=8, p=1)
    
    # Create AES cipher
    cipher = AES.new(key, AES.MODE_GCM, iv)
    
    # Decrypt the message and verify the tag
    decrypted_message = cipher.decrypt_and_verify(encrypted_message, tag)
    
    return decrypted_message.decode()

# Example usage
message = "Hello, World!"
password = "mysecretpassword"

encrypted = encrypt_message(message, password)
print("Encrypted:", encrypted)

decrypted = decrypt_message(encrypted, password)
print("Decrypted:", decrypted)
