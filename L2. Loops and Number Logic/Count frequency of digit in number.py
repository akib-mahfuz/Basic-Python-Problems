# Problem: Count frequency of digit in number.

num = input("Give a number: ")

cnt_list = []

for i in num:
    if i not in cnt_list:
        cnt = 0
        for j in num:
            if j == i:
                cnt += 1
        print(f"No of {i} = {cnt}")
        cnt_list.append(i)
    

