# UDF to modify the list (for example, doubling each element)
def modify_list(input_list):
    # Double each element in the list
    for i in range(len(input_list)):
        input_list[i] *= 2
    return input_list

# Main program
original_list = [1, 2, 3, 4, 5]
print("Original List:", original_list)

# Pass the list to the UDF and get the modified list
modified_list = modify_list(original_list)
print("Modified List:", modified_list)
