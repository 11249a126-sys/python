sentence = input("Enter a sentence: ")

words = sentence.split()
word_count = len(words)

digit_count = 0
upper_count = 0
lower_count = 0

for ch in sentence:
    if ch.isdigit():
        digit_count += 1
    elif ch.isupper():
        upper_count += 1
    elif ch.islower():
        lower_count += 1

print("Number of words:", word_count)
print("Number of digits:", digit_count)
print("Number of uppercase letters:", upper_count)
print("Number of lowercase letters:", lower_count)
