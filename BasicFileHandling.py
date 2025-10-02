# Basic File Handling Program: Find and Replace Words

def find_and_replace(file_name, old_word, new_word):
    try:
        # Open the file in read mode and read its content
        with open(file_name, 'r') as file:
            data = file.read()
        
        # Replace the old word with the new word
        modified_data = data.replace(old_word, new_word)
        
        # Save the modified data back to the same file
        with open(file_name, 'w') as file:
            file.write(modified_data)
        
        print(f"'{old_word}' has been replaced with '{new_word}'.")
    
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main program
def main():
    print("Basic File Handling: Find and Replace Words")
    file_name = input("Enter the file name (e.g., example.txt): ")
    old_word = input("Enter the word to be replaced: ")
    new_word = input("Enter the new word: ")
    
    find_and_replace(file_name, old_word, new_word)

if __name__ == "__main__":
    main()
