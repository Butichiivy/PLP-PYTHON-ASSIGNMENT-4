def read_and_modify_file(filename):
    try:
        # Try to open and read the file
        with open(filename, 'r') as file:
            lines = file.readlines()

        # Modify the content (for example, convert to uppercase)
        modified_lines = [line.upper() for line in lines]

        # Write to a new file
        new_filename = f"modified_{filename}"
        with open(new_filename, 'w') as new_file:
            new_file.writelines(modified_lines)

        print(f"File has been modified and saved as '{new_filename}'.")

    except FileNotFoundError:
        print("Error: The file was not found.")
    except IOError:
        print("Error: The file could not be read or written.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Ask the user for a filename
user_filename = input("Enter the filename to read and modify: ")
read_and_modify_file(user_filename)
