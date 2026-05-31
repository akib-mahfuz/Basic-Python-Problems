N = int(input("Enter number to calculate sum of even number: "))
total = 0
for i in range(1, N+1,2):
    total = total + i
print(f"Sum of even numbr upto {N} is {total}")
