base = int(input("Give base: "))
exponent = int(input("Give exponent: "))\

result = 1

for _ in range(exponent):
    result = result * base

print(f"{base} exponent {exponent} is {result}")