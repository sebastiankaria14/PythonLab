rows = int(input("Enter number of rows: "))

print("\nNumber Pattern:")
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("\nStar Pattern:")
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()
