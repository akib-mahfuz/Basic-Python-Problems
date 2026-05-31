n = int(input("Enter a number: "))

fact = 1
total = 0

for i in range(1,n+1):
    fact = fact * i
    total = total + fact

print(f"Factorial of {n} is {total}")
 