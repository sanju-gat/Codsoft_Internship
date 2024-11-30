# Task 3
# Password Generator


import random
import tkinter as tk
from tkinter import messagebox

def generate_password(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    password = "".join(random.choice(characters) for _ in range(length))
    return password

def on_generate_button_click():
    try:
        length = int(length_entry.get())
        if length < 1:
            raise ValueError("Password length must be greater than 0.")
        password = generate_password(length)
        password_entry.config(state=tk.NORMAL)
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
        password_entry.config(state='readonly')
    except ValueError as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Password Generator")
root.geometry("300x150")  # Set window size to 400x200


length_label = tk.Label(root, text="Enter the desired length for the password:")
length_label.pack(padx=10, pady=5)

length_entry = tk.Entry(root)
length_entry.pack(padx=10, pady=5)

generate_button = tk.Button(root, text="Generate Password", command=on_generate_button_click)
generate_button.pack(padx=10, pady=10)

password_entry = tk.Entry(root, state='readonly')
password_entry.pack(padx=10, pady=10)


root.mainloop()