# Smallest among Three Numbers

n1, n2, n3 = map(int, input("Give three Numbers: ").split())

# smallest = min(n1, n2, n3)

if n1 < n2 and n1 < n2:
    smallest = n1
elif n2 < n1 and n2 < n3:
    smallest = n2
else:
    smallest = n3

print(f"Smallest number is {smallest}")
