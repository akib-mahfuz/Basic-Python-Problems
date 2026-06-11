# Problem: Product of digits.

n = input("Give a digit: ")
l = len(n)
product = 1
for i in range(0,l):
    product = product * int(n[i])

print(f"Sum of digits is {product}")
