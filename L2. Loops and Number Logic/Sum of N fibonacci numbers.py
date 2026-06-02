# Sum of first N Fibonacci numbers

n = int(input("Enter number to find sum of N fibonacci number: "))

fir_num = 0
sec_num = 1
sum = 0

for i in range (0, n):
    sum += fir_num
    next = fir_num + sec_num
    fir_num = sec_num
    sec_num = next
    
print(sum)