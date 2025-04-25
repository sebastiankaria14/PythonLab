my_list = [1, 2.5, "hello", True, 3, "world", False, 7.9, 10, None]

int_count = 0
float_count = 0
str_count = 0
bool_count = 0
none_count = 0
other_count = 0

for item in my_list:
    if type(item) == int:
        int_count += 1
    elif type(item) == float:
        float_count += 1
    elif type(item) == str:
        str_count += 1
    elif type(item) == bool:
        bool_count += 1
    elif item is None:
        none_count += 1
    else:
        other_count += 1

print("Count of data types in the list:")
print("Integers:", int_count)
print("Floats:", float_count)
print("Strings:", str_count)
print("Booleans:", bool_count)
print("NoneType:", none_count)
print("Others:", other_count)
