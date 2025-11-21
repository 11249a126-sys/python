import difflib

def string_similarity(str1, str2):
    return difflib.SequenceMatcher(None, str1, str2).ratio()

# Main program
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

similarity = string_similarity(s1, s2)
print("String similarity:", similarity)
