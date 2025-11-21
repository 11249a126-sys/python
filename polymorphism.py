class Palindrome:
    def __init__(self, value):
        self.value = value

    def is_palindrome(self):
        pass  # This will be overridden in derived classes


# Derived class for strings
class StringPalindrome(Palindrome):
    def is_palindrome(self):
        # Remove spaces and convert to lowercase for proper string comparison
        cleaned = ''.join(self.value.split()).lower()
        return cleaned == cleaned[::-1]


# Derived class for integers
class IntegerPalindrome(Palindrome):
    def is_palindrome(self):
        value_str = str(self.value)
        return value_str == value_str[::-1]
