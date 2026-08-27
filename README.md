# File-Encryption-App-Project

Welcome to the **File Encryption App**, a secure and straightforward desktop application designed to keep your private files safe. With a user-friendly GUI, you can easily lock and unlock your files using a secure password. 

![App Interface](./assets/gui.png)

## Features
- **Secure Encryption**: Uses robust Fernet (AES-128) encryption. 
- **On-Demand Passwords**: Prompts for a password only when you need to encrypt or decrypt, ensuring security without maintaining global state. 
- **Consistent Keys**: Derives a 32-byte key automatically from your password using SHA-256 to reliably secure your files. 
- **Batch Processing**: Select and encrypt/decrypt multiple files at once. 

## Requirements
Ensure you have the following installed before running the app:
- Python 3.x
- `cryptography` library (Install using `pip install cryptography`)

## How to Use
1. **Run the App**: Execute `python "PYTHON PROJECT FINAL.py"` in your terminal.
2. **Encrypt**: Click the 'Encrypt' button, type a secure password, and select the files you wish to lock.
3. **Decrypt**: Click the 'Decrypt' button, type the same secure password, and select your locked files to restore them.

Keep your files safe and secure.
