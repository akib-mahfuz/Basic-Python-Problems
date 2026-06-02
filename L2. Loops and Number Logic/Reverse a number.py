# Problem: Reverse a number

num = int(input("Give a number: "))
n = num
reverse = 0

while n > 0:
    rem = n % 10
    n = n // 10
    reverse = reverse * 10 + rem
print(f"Reverse of {num} is {reverse}")
