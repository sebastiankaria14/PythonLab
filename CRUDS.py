import sqlite3


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
    conn.commit() # save changes
    conn.close() # Close the connection


# Add user
def add_user():
    username = input("Enter username: ")
    email = input("Enter email: ")
    password = input("Enter password: ")

    # Validation
    if not username or not email or not password:
        print("All fields are required!")
        return

    # Check if username already exists
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE username = ?', (username,))
    existing_user = c.fetchone()

    # Check if email already exists
    if existing_user:
        print("Username already exists! Please choose a different username.")
        conn.close()
        return

    c.execute('INSERT INTO users (username, email, password) VALUES (?, ?, ?)', (username, email, password))
    conn.commit()
    conn.close()
    print(f"User {username} added successfully!")


# Show all users
def show_users():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users')
    users = c.fetchall()

    if users:
        # Print all users
        print("\nAll Users:")
        for user in users:
            print(f"ID: {user[0]}, Username: {user[1]}, Email: {user[2]}")
    else:
        print("No users found.")

    conn.close()


# Delete user
def delete_user():
    username = input("Enter username to delete: ")

    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE username = ?', (username,))
    user = c.fetchone()

    if user:
        c.execute('DELETE FROM users WHERE username = ?', (username,))
        conn.commit()
        print(f"User {username} deleted successfully!")
    else:
        print(f"No user found with username: {username}")

    conn.close()


# Update user
def update_user():
    username = input("Enter username to update: ")

    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE username = ?', (username,))
    user = c.fetchone()

    if user:
        # Print current email and ask for new email
        new_email = input(f"Enter new email for {username} (Current: {user[2]}): ")
        new_password = input(f"Enter new password for {username}: ")

        c.execute('UPDATE users SET email = ?, password = ? WHERE username = ?', (new_email, new_password, username))
        conn.commit()
        print(f"User {username} updated successfully!")
    else:
        print(f"No user found with username: {username}")

    conn.close()


# Search user
def search_user():
    username = input("Enter username to search: ")

    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE username = ?', (username,))
    user = c.fetchone()

    if user:
        print(f"User found: ID: {user[0]}, Username: {user[1]}, Email: {user[2]}")
    else:
        print(f"No user found with username: {username}")

    conn.close()


# Main menu
def main_menu():
    while True:
        print("\nUser Management System")
        print("1. Add User")
        print("2. Show All Users")
        print("3. Delete User")
        print("4. Update User")
        print("5. Search User")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_user()
        elif choice == "2":
            show_users()
        elif choice == "3":
            delete_user()
        elif choice == "4":
            update_user()
        elif choice == "5":
            search_user()
        elif choice == "6":
            print("Exiting User Management System...")
            break
        else:
            print("Invalid choice! Please try again.")


# Initialize the database and the application
create_table()
main_menu()

