file_name = input("Enter the file name: ")

try:
    with open(file_name, 'r') as file:
        lines = file.readlines()

    # Display first N lines
    N = int(input("Enter the number of lines to display from the start: "))
    print(f"\nFirst {N} lines of the file:")
    for i in range(min(N, len(lines))):
        print(lines[i], end='')

    # Find frequency of a word
    word_to_search = input("\n\nEnter the word to find its frequency: ")
    word_count = sum(line.lower().split().count(word_to_search.lower()) for line in lines)
    print(f"The word '{word_to_search}' occurs {word_count} times in the file.")

except FileNotFoundError:
    print(f"Error: The file '{file_name}' does not exist.")
