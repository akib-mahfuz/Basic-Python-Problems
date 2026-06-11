#  Check if a number is power of 2

num = int(input("Give number: "))
n = num

if n < 0:
    result = False
else:
    while n % 2 == 0:
        n = n // 2
    result = (n == 1)

if result:
    print(f"{n} is a power of 2")
else:
    print(f"{n} is not a power of 2")



