# Largest among Three Numbers

n1, n2, n3 = map(int, input("Give three Numbers: ").split())

# largest = max(n1, n2, n3)

if n1 > n2 and n1 > n2:
    largest = n1
elif n2 > n1 and n2 > n3:
    largest = n2
else:
    largest = n3

print(f"Largest number is {largest}")
