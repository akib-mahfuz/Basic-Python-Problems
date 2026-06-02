# Problem: Check whether a number belongs to the Fibonacci sequence

n = int(input("Enter number to find sum of N fibonacci number: "))

fir_num = 0
sec_num = 1
fibbo_list = []

while fir_num <= n:
    next = fir_num + sec_num
    fir_num = sec_num
    sec_num = next
    fibbo_list.append(fir_num)

if n in fibbo_list:
    print("Yes")
else:
    print("No")
    
