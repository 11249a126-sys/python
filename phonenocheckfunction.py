def isPhoneNumber(text):
    # Pattern: 415-555-4242  (12 characters)
    if len(text) != 12:
        return False

    # Check first 3 characters are digits
    if not text[0:3].isdigit():
        return False
    
    # Check dash
    if text[3] != '-':
        return False
    
    # Check next 3 digits
    if not text[4:7].isdigit():
        return False
    
    # Check dash
    if text[7] != '-':
        return False
    
    # Check last 4 digits
    if not text[8:12].isdigit():
        return False

    return True


# Example
print(isPhoneNumber("415-555-4242"))  # True
print(isPhoneNumber("123-45-6789"))   # False
