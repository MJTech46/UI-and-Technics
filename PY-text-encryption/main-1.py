# no installation needed
import hashlib
import base64

def encrypt_message(message, password):
    # Create a SHA-256 hash of the password
    key = hashlib.sha256(password.encode()).digest()
    
    # XOR the message bytes with the key
    encrypted_message = bytes([message[i] ^ key[i % len(key)] for i in range(len(message))])
    
    # Encode the encrypted message in base64 for readability
    return base64.b64encode(encrypted_message).decode()

def decrypt_message(encoded_message, password):
    # Decode the base64 encoded message
    encrypted_message = base64.b64decode(encoded_message)
    
    # Create a SHA-256 hash of the password
    key = hashlib.sha256(password.encode()).digest()
    
    # XOR the encrypted message bytes with the key
    decrypted_message = bytes([encrypted_message[i] ^ key[i % len(key)] for i in range(len(encrypted_message))])
    
    return decrypted_message.decode()

# Example usage
message = "Hello, World!"
password = "mysecretpassword"

encrypted = encrypt_message(message.encode(), password)
print("Encrypted:", encrypted)
print("type: ", type(encrypted))

decrypted = decrypt_message(encrypted, password)
print("Decrypted:", decrypted)
print("type: ", type(decrypted))
