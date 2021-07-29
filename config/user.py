from cryptography.fernet import Fernet

# Encrypt password config
key = Fernet.generate_key()
key_f = Fernet(key)