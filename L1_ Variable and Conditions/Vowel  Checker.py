char = input("Give an alphabet: ").lower()
vowel = ["a", "e", "i", "o", "u"]

if char in vowel:
    print(f"{char} is a vowel")
else:
    print(f"{char} is not a vowel")
