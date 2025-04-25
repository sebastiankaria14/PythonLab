def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Main program
terms = int(input("Enter number of Fibonacci terms to display: "))

print("\nFibonacci Series:")
for i in range(terms):
    print(fibonacci(i), end=' ')
