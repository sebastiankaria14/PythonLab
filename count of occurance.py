my_list = [5, 3, 7, 3, 9, 3, 1, 4, 3]

value = int(input("Enter the value to search: "))

count = 0
indices = []

for i in range(len(my_list)):
    if my_list[i] == value:
        count += 1
        indices.append(i)

if count > 0:
    print(f"\nThe value {value} occurred {count} times.")
    print("Index positions:", indices)
else:
    print(f"\nThe value {value} was not found in the list.")
