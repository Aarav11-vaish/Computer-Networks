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
