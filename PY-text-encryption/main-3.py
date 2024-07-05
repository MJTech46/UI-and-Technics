# install 'pyAesCrypt'
import pyAesCrypt
import io
import base64

def encrypt_message(message, password):
    # Create an in-memory bytes buffer
    buffer = io.BytesIO()
    
    # Encrypt the message
    pyAesCrypt.encryptStream(io.BytesIO(message.encode()), buffer, password, bufferSize=64*1024)
    
    # Get the encrypted message
    encrypted_message = buffer.getvalue()
    
    # Encode the encrypted message in base64 for readability
    return base64.b64encode(encrypted_message).decode()

def decrypt_message(encrypted_message, password):
    # Decode the base64 encoded message
    encrypted_message = base64.b64decode(encrypted_message)
    
    # Create an in-memory bytes buffer
    buffer = io.BytesIO(encrypted_message)
    
    # Decrypt the message
    decrypted_buffer = io.BytesIO()
    pyAesCrypt.decryptStream(buffer, decrypted_buffer, password, bufferSize=64*1024) #, encSize=len(encrypted_message))
    
    # Get the decrypted message
    decrypted_message = decrypted_buffer.getvalue().decode()
    
    return decrypted_message

# Example usage
message = "Hello, World!"
password = "mysecretpassword"

encrypted = encrypt_message(message, password)
print("Encrypted:", encrypted)
print("type: ", type(encrypted))

decrypted = decrypt_message(encrypted, password)
print("Decrypted:", decrypted)
print("type: ", type(decrypted))
