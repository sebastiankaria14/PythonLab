# math_operations.py

# Function to calculate factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Function to check if a number is prime
def prime_number(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Function to calculate power
def pow_number(base, exponent):
    return base ** exponent

# menu_driven.py
import math_operations as mo

def display_menu():
    print("\nMenu:")
    print("1. Calculate Factorial")
    print("2. Check Prime Number")
    print("3. Calculate Power")
    print("4. Exit")

# Main program
while True:
    display_menu()
    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        num = int(input("Enter a number to find factorial: "))
        print(f"Factorial of {num} is {mo.factorial(num)}")

    elif choice == 2:
        num = int(input("Enter a number to check if it's prime: "))
        if mo.prime_number(num):
            print(f"{num} is a prime number.")
        else:
            print(f"{num} is not a prime number.")

    elif choice == 3:
        base = float(input("Enter base: "))
        exponent = float(input("Enter exponent: "))
        print(f"{base} raised to the power of {exponent} is {mo.pow_number(base, exponent)}")

    elif choice == 4:
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")

'''
CREATE AS maths_operations.py then import math_operations as mo
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"
'''