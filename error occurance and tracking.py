def find_errors_in_log(log_file, output_file):
    try:
        # Open the log file and the output file
        with open(log_file, 'r') as log, open(output_file, 'w') as output:
            line_number = 0
            error_count = 0
            
            # Iterate through each line in the log file
            for line in log:
                line_number += 1
                # Check if 'error' is in the line (case insensitive)
                if 'error' in line.lower():
                    error_count += 1
                    # Write the line number and content of the line with 'error' to output file
                    output.write(f"Line {line_number}: {line}")
            
            # After processing, log the count of errors found
            output.write(f"\nTotal occurrences of 'error': {error_count}\n")
            print(f"Processing complete. {error_count} occurrences of 'error' found. Check 'error.txt' for details.")
    
    except FileNotFoundError:
        print(f"Error: The file '{log_file}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    log_file = 'server.txt'  # Replace with your actual log file name
    output_file = 'error.txt'
    
    # Call function to find errors in the log and write to error.txt
    find_errors_in_log(log_file, output_file)

# Run the program
main()
