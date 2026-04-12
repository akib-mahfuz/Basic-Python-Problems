# Check Numbers divisable by 5 & 11.

num = int(input("Enter number: "))
if num % 5 == 0 and num % 11 == 0:
    print(f"{num} is divisable by 5 and 11")
else:
    print(f"{num} is not divisable by 5 and 11")
