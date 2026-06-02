# Check prime number.
n = int(input("Give number to check prime number or not: "))


if n < 2:
    print("Not prime number")
else:
    for i in range(2, n):
        if n % i == 0:
            print("Not prime number")
            break
    else:
        print("Prime Number")