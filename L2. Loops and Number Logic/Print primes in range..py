# Print primes in range.

n = int(input("Give number to print prime number in range: "))

prime_list = []

for i in range(2, n+1):
    for j in range (2,i):
        if i %j == 0:
            break
    else:
        prime_list.append(i)

print(prime_list)
            