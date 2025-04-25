import sqlite3
import tkinter as tk
from tkinter import messagebox
import re
from hashlib import sha256

# Database setup
def create_table():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        email TEXT NOT NULL,
        password TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

# Function to register a new user
def register_user():
    username = entry_username.get()
    email = entry_email.get()
    password = entry_password.get()
    confirm_password = entry_confirm_password.get()

    # Validation
    if not username or not email or not password or not confirm_password:
        messagebox.showerror("Error", "All fields are required!")
        return

    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match!")
        return

    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        messagebox.showerror("Error", "Invalid email format!")
        return

    hashed_password = sha256(password.encode()).hexdigest()

    conn = sqlite3.connect('users.db')
    c = conn.cursor()

    try:
        c.execute('INSERT INTO users (username, email, password) VALUES (?, ?, ?)', (username, email, hashed_password))
        conn.commit()
        messagebox.showinfo("Success", "Registration successful!")
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Username already exists!")
    finally:
        conn.close()

# Function to login an existing user
def login_user():
    username = entry_username_login.get()
    password = entry_password_login.get()

    if not username or not password:
        messagebox.showerror("Error", "Both fields are required!")
        return

    hashed_password = sha256(password.encode()).hexdigest()

    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, hashed_password))
    user = c.fetchone()

    if user:
        messagebox.showinfo("Success", "Login successful!")
    else:
        messagebox.showerror("Error", "Invalid username or password!")
    conn.close()

# Tkinter GUI setup with colors and bigger textboxes
def register_window():
    global entry_username, entry_email, entry_password, entry_confirm_password

    window = tk.Tk()
    window.title("Register")
    window.geometry("500x500")  # Set window size bigger
    window.config(bg="#f0f0f0")  # Background color

    #user entry
    tk.Label(window, text="Username", bg="#f0f0f0", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10)
    entry_username = tk.Entry(window, font=("Arial", 12), width=25)
    entry_username.grid(row=0, column=1, padx=10, pady=10)

    #email enrty
    tk.Label(window, text="Email", bg="#f0f0f0", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=10)
    entry_email = tk.Entry(window, font=("Arial", 12), width=25)
    entry_email.grid(row=1, column=1, padx=10, pady=10)

    #password entry
    tk.Label(window, text="Password", bg="#f0f0f0", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=10)
    entry_password = tk.Entry(window, show="*", font=("Arial", 12), width=25)
    entry_password.grid(row=2, column=1, padx=10, pady=10)

    #confirm password entry 
    tk.Label(window, text="Confirm Password", bg="#f0f0f0", font=("Arial", 12)).grid(row=3, column=0, padx=10, pady=10)
    entry_confirm_password = tk.Entry(window, show="*", font=("Arial", 12), width=25)
    entry_confirm_password.grid(row=3, column=1, padx=10, pady=10)

    # Register button
    tk.Button(window, text="Register", command=register_user, bg="#4CAF50", fg="white", font=("Arial", 12), width=20).grid(row=4, column=0, columnspan=2, pady=20)

    window.mainloop()

# Gui for login
def login_window():
    global entry_username_login, entry_password_login

    window = tk.Tk()
    window.title("Login")
    window.geometry("500x400")  # Set window size bigger
    window.config(bg="#f0f0f0")  # Background color

    # Username and password entry
    tk.Label(window, text="Username", bg="#f0f0f0", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10)
    entry_username_login = tk.Entry(window, font=("Arial", 12), width=25)
    entry_username_login.grid(row=0, column=1, padx=10, pady=10)

    # Password entry
    tk.Label(window, text="Password", bg="#f0f0f0", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=10)
    entry_password_login = tk.Entry(window, show="*", font=("Arial", 12), width=25)
    entry_password_login.grid(row=1, column=1, padx=10, pady=10)

    # Login button
    tk.Button(window, text="Login", command=login_user, bg="#4CAF50", fg="white", font=("Arial", 12), width=20).grid(row=2, column=0, columnspan=2, pady=20)

    window.mainloop()

# Main menu window with buttons for Login and Register
def main_menu():
    root = tk.Tk()
    root.title("Main Menu")
    root.geometry("400x300")  # Set window size bigger
    root.config(bg="#f0f0f0")  # Background color

    tk.Button(root, text="Login", command=login_window, bg="#4CAF50", fg="white", font=("Arial", 12), width=20).pack(pady=20)
    tk.Button(root, text="Register", command=register_window, bg="#4CAF50", fg="white", font=("Arial", 12), width=20).pack(pady=20)

    root.mainloop()

# Initialize the database and the application
create_table()
main_menu()
