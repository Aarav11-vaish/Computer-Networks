import socket
import rsa
import os

# Load the server's public key from file
def load_public_key():
    with open("public_key.pem", "rb") as pub_file:
        public_key = rsa.PublicKey.load_pkcs1(pub_file.read())
    return public_key

def send_document(host='127.0.0.1', port=65432, document_path='document.txt'):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        print(f"Connected to server at {host}:{port}.")

        # Read the content of the document
        with open(document_path, 'rb') as f:
            document_content = f.read()

        # Send the document content to the server
        s.sendall(document_content)
        print(f"Sent document '{document_path}' to the server.")

        # Receive the signature from the server
        signature = s.recv(1024)
        print("Received signature from the server.")

        # Save the signature to a file
        signature_path = f"{document_path}.sig"
        with open(signature_path, 'wb') as sig_file:
            sig_file.write(signature)
        print(f"Signature saved as '{signature_path}'.")

        return signature_path

# Input for document content
document_content = input("Enter the content for the document: ")

# Create the document file
document_path = 'document.txt'
with open(document_path, 'w') as doc_file:
    doc_file.write(document_content)
print(f"Test document created as '{document_path}'.")

# Send the document to the server and get the signature
signature_path = send_document(host='127.0.0.1', port=65432, document_path=document_path)

# Load the public key for verification
public_key = load_public_key()

# Optionally, verify the signature
with open(signature_path, 'rb') as sig_file:
    received_signature = sig_file.read()

# Verify the signature
try:
    rsa.verify(open(document_path, 'rb').read(), received_signature, public_key)
    print(f"Signature valid for '{document_path}': True")
except rsa.VerificationError:
    print(f"Signature valid for '{document_path}': False")
