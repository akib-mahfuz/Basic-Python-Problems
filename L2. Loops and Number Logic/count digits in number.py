# Count digits in a number.

n = input("Enter number: ")

#Method 1
digit = 0
for i in n:
    digit = digit + 1

#Method 2
#digit = len(n) 

print(f"Total digits are {digit}")