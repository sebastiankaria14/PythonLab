def write_to_file():
    # Accept file name and content from the user
    file_name = input("Enter the file name (with extension): ")
    content = input("Enter the content you want to write to the file: ")

    # Write the content to the file
    with open(file_name, 'w') as file:
        file.write(content)
    print(f"Content has been written to {file_name}")

def read_using_read(file_name):
    # Read entire content of the file using read()
    with open(file_name, 'r') as file:
        content = file.read()
    print("\nContent using 'read()':")
    print(content)

def read_using_readline(file_name):
    # Read file line by line using readline()
    with open(file_name, 'r') as file:
        print("\nContent using 'readline()':")
        line = file.readline()
        while line:
            print(line.strip())  # strip() removes the trailing newline
            line = file.readline()

def read_using_with_open(file_name):
    # Read the file using the with open() approach
    with open(file_name, 'r') as file:
        print("\nContent using 'with open()':")
        for line in file:
            print(line.strip())

def main():
    # Step 1: Write to file
    write_to_file()

    # Step 2: Accept file name to read content
    file_name = input("\nEnter the file name (with extension) to read content: ")

    # Step 3: Display the content using 3 different methods
    read_using_read(file_name)
    read_using_readline(file_name)
    read_using_with_open(file_name)

# Run the main function
main()
