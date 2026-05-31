N = int(input("Enter number to calculate sum of natural number: "))
sum = 0
for i in range(1, N+1):
    sum = sum + i
print(f"Sum upto {N} is {sum}")
