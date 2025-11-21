num = input("Enter a number: ")

# Palindrome check
if num == num[::-1]:
    print(num, "is a palindrome.")
else:
    print(num, "is not a palindrome.")

# Counting digit occurrences
print("Digit occurrences:")
for digit in set(num):
    print(digit, ":", num.count(digit))
