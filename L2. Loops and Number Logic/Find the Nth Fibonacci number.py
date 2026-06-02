# Find the Nth Fibonacci number

n = int(input("Enter number to find N th fibonacci number: "))

fir_num = 0
sec_num = 1

for i in range (1, n):
    next = fir_num + sec_num
    fir_num = sec_num
    sec_num = next
    
print(fir_num)

