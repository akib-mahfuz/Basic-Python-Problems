n = int(input("Enter a number to print its multiplication table: "))
limit = int(input("Enter the table limit: "))

for i in range (1, limit+1):
    print(f"{n} * {i} = {n * i}")
