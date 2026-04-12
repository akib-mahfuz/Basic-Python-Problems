# Check Alphabet or not

# Method 1
letter = input("Enter alphabet: ")

if ("A" <= letter <= "Z") or ("a" <= letter <= "z"):
    print(f"{letter} is an alphabet")
else:
    print(f"{letter} is not an alphabet")

# Method 2
"""
if letter.isalpha():
    print(f"{letter} is an alphabet")

else:
    print(f"{letter} is not an alphabet")

"""
