text = input("Enter a string: ")

vowels = consonants = spaces = digits = specials = 0

for ch in text:
    if ch.lower() in 'aeiou':
        vowels += 1
    elif ch.isalpha():
        consonants += 1
    elif ch.isdigit():
        digits += 1
    elif ch.isspace():
        spaces += 1
    else:
        specials += 1

print("\nAnalysis of the string:")
print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Blank Spaces:", spaces)
print("Special Symbols:", specials)
