from tkinter import *
from tkinter import messagebox, filedialog, simpledialog
from cryptography.fernet import Fernet

# Set global variables
global password
global fernet


# Generates the key from the provided password
def generate_key_from_password(password):
    key = Fernet.generate_key()
    fernet = Fernet(key)
    return fernet


# Prompts the user to enter a password for encryption/decryption
def prompt_password():
    global password
    global fernet

    password = simpledialog.askstring("Enter Password", "Enter the password:")
    if not password:
        messagebox.showerror("Error", "No password entered, try again")
        return

    fernet = generate_key_from_password(password)
    messagebox.showinfo("", "Password set successfully!")


# Function to encrypt files of your choosing
def encrypt():
    global password
    global fernet

    if not password:
        messagebox.showerror("Error", "Password not set, please set a password first")
        return

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
    global password
    global fernet

    if not password:
        messagebox.showerror("Error", "Password not set, please set a password first")
        return

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

# Labels
password_label = Label(top, text="Password:", bg="#D9E3DA")
password_label.pack(pady=10)

# Set Password button
password_button = Button(top, text="Set Password", command=prompt_password, bg="#4CAF50", fg="white")
password_button.pack(pady=10)

# Encrypt and Decrypt buttons
encrypt_button = Button(top, text="Encrypt", command=encrypt, bg="#008CBA", fg="white")
encrypt_button.pack(pady=10)

decrypt_button = Button(top, text="Decrypt", command=decrypt, bg="#008CBA", fg="white")
decrypt_button.pack(pady=10)

# Loop GUI window
top.mainloop()
