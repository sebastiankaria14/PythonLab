my_list = [12, 5, 8, 1, 19, 3]

print("Original List:", my_list)
choice = int(input("Press 1 for ascending order or 2 for descending order: "))

if choice == 1:
    my_list.sort()
    print("List sorted in ascending order:", my_list)
elif choice == 2:
    my_list.sort(reverse=True)
    print("List sorted in descending order:", my_list)
else:
    print("Invalid choice.")