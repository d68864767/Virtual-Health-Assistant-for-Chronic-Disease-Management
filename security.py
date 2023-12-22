# Importing necessary libraries
from cryptography.fernet import Fernet
import os

class Security:
    def __init__(self):
        self.key = os.environ.get('SECRET_KEY')
        self.cipher_suite = Fernet(self.key)

    def encrypt_data(self, data):
        """
        Function to encrypt sensitive data.
        This involves converting the data into bytes and then encrypting it using the Fernet encryption method.
        """
        # Convert the data into bytes
        data_bytes = data.encode('utf-8')

        # Encrypt the data
        encrypted_data = self.cipher_suite.encrypt(data_bytes)

        return encrypted_data

    def decrypt_data(self, encrypted_data):
        """
        Function to decrypt encrypted data.
        This involves decrypting the data using the Fernet decryption method and then converting it back into a string.
        """
        # Decrypt the data
        decrypted_data = self.cipher_suite.decrypt(encrypted_data)

        # Convert the data back into a string
        data = decrypted_data.decode('utf-8')

        return data

    def secure_request(self, request):
        """
        Function to secure a request to the EHR API.
        This involves encrypting the request data and adding a secure header to the request.
        """
        # Encrypt the request data
        encrypted_data = self.encrypt_data(request.data)

        # Add a secure header to the request
        request.headers['X-Secure'] = 'True'

        return request

    def secure_response(self, response):
        """
        Function to secure a response from the EHR API.
        This involves encrypting the response data.
        """
        # Encrypt the response data
        encrypted_data = self.encrypt_data(response.data)

        return encrypted_data

security = Security()

def encrypt_data(data):
    return security.encrypt_data(data)

def decrypt_data(encrypted_data):
    return security.decrypt_data(encrypted_data)

def secure_request(request):
    return security.secure_request(request)

def secure_response(response):
    return security.secure_response(response)
