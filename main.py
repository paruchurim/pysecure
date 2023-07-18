from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    return key

def encrypt_message(key, message):
    cipher_suite = Fernet(key)
    encrypted_message = cipher_suite.encrypt(message.encode('utf-8'))
    return encrypted_message

def decrypt_message(key, encrypted_message):
    cipher_suite = Fernet(key)
    decrypted_message = cipher_suite.decrypt(encrypted_message)
    return decrypted_message.decode('utf-8')

# Example usage
key = generate_key()
message = "This is a secret message"
encrypted_message = encrypt_message(key, message)
print(encrypted_message)
decrypted_message = decrypt_message(key, encrypted_message)
print(decrypted_message)
