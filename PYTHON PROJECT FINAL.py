from tkinter import *
from tkinter import messagebox, filedialog, simpledialog
from cryptography.fernet import Fernet
import base64
import hashlib


# Generates the key from the provided password
def generate_key_from_password(password):
    hashed_password = hashlib.sha256(password.encode()).digest()
    key = base64.urlsafe_b64encode(hashed_password)
    fernet = Fernet(key)
    return fernet


# Function to encrypt files of your choosing
def encrypt():
    password = simpledialog.askstring("Enter Password", "Enter a password to lock the files:", show='*')
    if not password:
        messagebox.showwarning("Cancelled", "No password entered. Encryption cancelled.")
        return
        
    fernet = generate_key_from_password(password)

    messagebox.showinfo("", "Select one or more files to encrypt")
    filepath = filedialog.askopenfilenames()

    for x in filepath:
        with open(x, "rb") as file:
            original = file.read()

        encrypted = fernet.encrypt(original)

        with open(x, "wb") as encrypted_file:
            encrypted_file.write(encrypted)

    if not filepath:
        messagebox.showerror("Error", "No file selected, try again")
    else:
        messagebox.showinfo("", "Files encrypted successfully!")


# Function to decrypt files of your choosing
def decrypt():
    password = simpledialog.askstring("Enter Password", "Enter the password to unlock the files:", show='*')
    if not password:
        messagebox.showwarning("Cancelled", "No password entered. Decryption cancelled.")
        return
        
    fernet = generate_key_from_password(password)

    messagebox.showinfo("", "Select one or more files to decrypt")
    filepath = filedialog.askopenfilenames()

    for x in filepath:
        with open(x, "rb") as enc_file:
            encrypted = enc_file.read()

        decrypted = fernet.decrypt(encrypted)

        with open(x, "wb") as dec_file:
            dec_file.write(decrypted)

    if not filepath:
        messagebox.showerror("Error", "No file selected, try again")
    else:
        messagebox.showinfo("", "Files decrypted successfully!")


# GUI setup
top = Tk()
top.geometry("400x300")
top.title("File Encryption App")

# Background color
top.configure(bg="#D9E3DA")

# GUI configuration completely simplified (removed password input from main window)

# Encrypt and Decrypt buttons
encrypt_button = Button(top, text="Encrypt", command=encrypt, bg="#008CBA", fg="white")
encrypt_button.pack(pady=10)

decrypt_button = Button(top, text="Decrypt", command=decrypt, bg="#008CBA", fg="white")
decrypt_button.pack(pady=10)

# Loop GUI window
top.mainloop()
