# LCM using loop.
a1= int(input("Give first number: "))
a2= int(input("Give second number: "))

n1 = min(a1, a2)
n2 = max(a1,a2)

i = 1

while True:
    if (n2 * i) % n1 ==0:
        lcm = n2 * i
        break
    i += 1

print(lcm)