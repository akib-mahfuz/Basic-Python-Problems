# Problem: Armstrong number check.

n = int(input("Give number: "))

sum = 0
temp = n
digits = len(str(n))

while temp > 0:
    num = temp % 10
    sum += num**digits
    temp = temp // 10

if sum == n:
    print(f"{n} is a Armstrong Number")
else:
    print(f"{n} is not a Armstrong Number")
