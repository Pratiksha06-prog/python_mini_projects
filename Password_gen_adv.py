#ADVANCED PASSWORD GENERATOR
import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate password
def generate_password():
    length = int(length_entry.get())
    use_letters = letters_var.get()
    use_digits = digits_var.get()
    use_symbols = symbols_var.get()

    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        messagebox.showwarning("Warning", "Please select at least one character type.")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# Function to copy to clipboard
def copy_password():
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# GUI setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.config(bg="#f2f2f2")

# Widgets
tk.Label(root, text="Password Length:", bg="#f2f2f2").pack(pady=5)
length_entry = tk.Entry(root)
length_entry.pack()

letters_var = tk.BooleanVar()
digits_var = tk.BooleanVar()
symbols_var = tk.BooleanVar()

tk.Checkbutton(root, text="Include Letters", variable=letters_var, bg="#f2f2f2").pack()
tk.Checkbutton(root, text="Include Digits", variable=digits_var, bg="#f2f2f2").pack()
tk.Checkbutton(root, text="Include Symbols", variable=symbols_var, bg="#f2f2f2").pack()

tk.Button(root, text="Generate Password", command=generate_password, bg="#4CAF50", fg="white").pack(pady=10)

password_entry = tk.Entry(root, width=30)
password_entry.pack()

tk.Button(root, text="Copy to Clipboard", command=copy_password, bg="#2196F3", fg="white").pack(pady=5)

# Run the GUI loop
root.mainloop()
