# Document Signing and Verification System

## Overview
- Client-server application for secure document signing and verification using RSA encryption.
- Server generates RSA key pair (public and private keys) if not present.
- Client sends document to server; server signs it and returns the signature.
- Client verifies document integrity and authenticity using server's public key.

## Features
- **RSA Key Generation**: Creates RSA public-private key pair if not present.
- **Document Transfer**: Sends document from client to server over TCP.
- **Document Signing**: Server signs document content with private key.
- **Signature Verification**: Client verifies signature using server's public key.

## Requirements
- Python 3.x
- `rsa` package for encryption and signing
- `socket` for network communication

```bash
pip install rsa
## Files
- `public_key.pem`: Stores RSA public key (auto-generated if not present).
- `private_key.pem`: Stores RSA private key (auto-generated if not present).
- `document.txt`: Temporary file for document content sent by client.
- `<document>.sig`: Signature file generated by server and saved by client.

## Code Components

### Client Code (`send_document` function in client file)
- Reads document content from `document.txt`.
- Sends content to server over TCP socket.
- Receives signature from server, saves it as `<document>.sig`.
- Verifies signature using public key.

### Server Code (`start_server` function in server file)
- Listens for incoming client connections.
- Receives document content, signs it with private key, returns signature to client.

## Usage

### Start the Server
```bash
python server.py

