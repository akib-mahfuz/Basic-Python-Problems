# Fibonacci series up to N terms.

n = int(input("Give number: "))

fir_num = 0
sec_num = 1

for i in range(1, n+1):
    print(f"{fir_num}")
    next_num = fir_num + sec_num
    fir_num = sec_num
    sec_num = next_num

