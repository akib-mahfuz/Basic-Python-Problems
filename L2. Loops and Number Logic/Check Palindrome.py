# Check palindrome number.
# Note: A number is a palindrome if it reads the same forwards and backwards

num = int(input("Give a number: "))
n = num
reverse = 0

while n > 0:
    rem = n % 10
    n = n // 10
    reverse = reverse * 10 + rem

if num == reverse:
    print(f"{num} is a palindrome number")
else:
    print(f"{num} is not a palindrome number")