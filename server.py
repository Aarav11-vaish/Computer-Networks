import socket
import rsa
import os

# Check if key files exist, if not create them
if not os.path.exists("public_key.pem") or not os.path.exists("private_key.pem"):
    # Generate a new RSA key pair
    public_key, private_key = rsa.newkeys(512)

    # Save the keys to files
    with open("public_key.pem", "wb") as pub_file:
        pub_file.write(public_key.save_pkcs1(format='PEM'))
    
    with open("private_key.pem", "wb") as priv_file:
        priv_file.write(private_key.save_pkcs1(format='PEM'))
else:
    # Load existing keys
    with open("public_key.pem", "rb") as pub_file:
        public_key = rsa.PublicKey.load_pkcs1(pub_file.read())
    
    with open("private_key.pem", "rb") as priv_file:
        private_key = rsa.PrivateKey.load_pkcs1(priv_file.read())

# Start the server
def start_server(host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"Server is listening on {host}:{port}...")
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            document_content = conn.recv(1024)
            print("Received document content.")

            # Sign the document
            signature = rsa.sign(document_content, private_key, 'SHA-256')
            print("Document signed.")

            # Send the signature back to the client
            conn.sendall(signature)
            print("Sent signature to the client.")

if __name__ == "__main__":
    start_server()
