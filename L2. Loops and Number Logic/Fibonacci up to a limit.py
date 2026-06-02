n = int(input("Enter number as limit of fibonacci series: "))

fir_num = 0
sec_num = 1

while fir_num < n:
    print(fir_num)
    next = fir_num + sec_num
    fir_num = sec_num
    sec_num = next


