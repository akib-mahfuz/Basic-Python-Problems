#Problem: Sum of digits

n = input("Give a digit: ")
l = len(n)
total = 0
for i in range(0,l):
    total = total + int(n[i])

print(f"Sum of digits is {total}")

