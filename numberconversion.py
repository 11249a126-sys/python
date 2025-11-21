def binary_to_decimal(binary_str):
    # Convert binary to decimal
    try:
        return int(binary_str, 2)
    except ValueError:
        return "Invalid binary number!"

def octal_to_hexadecimal(octal_str):
    # Convert octal to hexadecimal
    try:
        decimal_value = int(octal_str, 8)   # First convert octal to decimal
        return hex(decimal_value)[2:].upper()   # Convert decimal to hex
    except ValueError:
        return "Invalid octal number!"


# Main program
print("1. Binary to Decimal")
binary_input = input("Enter a binary number: ")
print("Decimal value:", binary_to_decimal(binary_input))

print("\n2. Octal to Hexadecimal")
octal_input = input("Enter an octal number: ")
print("Hexadecimal value:", octal_to_hexadecimal(octal_input))
