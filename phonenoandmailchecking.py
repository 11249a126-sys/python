import re

# Function to search for phone numbers and emails in a file
def search_contacts(file_path):
    # Regular expression patterns
    phone_pattern = r'\+?\d{1,3}\d{10}'  # Matches +919900889977 or 919900889977
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'  # Matches standard emails

    # Lists to store matches
    phones = []
    emails = []

    # Open and read the file
    with open(file_path, 'r') as file:
        for line in file:
            # Find all matches in the line
            phones.extend(re.findall(phone_pattern, line))
            emails.extend(re.findall(email_pattern, line))

    return phones, emails

# Example usage
file_path = 'sample.txt'  # Replace with your file path
phones, emails = search_contacts(file_path)

print("Phone Numbers Found:")
for phone in phones:
    print(phone)

print("\nEmail Addresses Found:")
for email in emails:
    print(email)
