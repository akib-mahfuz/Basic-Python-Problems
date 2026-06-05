# Problem: Check a number is perfect number or not
# A perfect number is a positive integer that equals the sum of its proper positive divisor

n = int(input("Give number: "))

total = 0

for i in range(1, n):
    if n % i == 0:
        total += i

if total == n:
    print(f"{n} is a perfect number")
else:
    print(f"{n} is not a perfect number")
