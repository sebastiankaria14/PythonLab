# Sample user database
users = {
    "admin": "admin123",
    "user1": "password1",
    "user2": "pass@456"
}

MAX_ATTEMPTS = 3
attempts = 0

print(" Secure Login System \n")

while attempts < MAX_ATTEMPTS:
    try:
        username = input("Enter username: ")
        password = input("Enter password: ")

        if not username or not password:
            raise ValueError("Username or password cannot be empty!")  # Handle empty input

        if username not in users:
            raise KeyError("User does not exist!")  # Handle unknown user

        if users[username] != password:
            raise PermissionError("Incorrect password!")  # Handle invalid password

        # If everything is fine
        print(f"\nLogin successful! Welcome, {username.capitalize()} ")
        break

    except ValueError as ve:
        print(f" ValueError: {ve}")

    except KeyError as ke:
        print(f" KeyError: {ke}")

    except PermissionError as pe:
        print(f" PermissionError: {pe}")

    except Exception as e:
        print(f" General Exception: {e}")

    finally:
        attempts += 1
        print(f"Attempts remaining: {MAX_ATTEMPTS - attempts}\n")

        if attempts == MAX_ATTEMPTS:
            print(" Too many login attempts! Access Denied. ")
