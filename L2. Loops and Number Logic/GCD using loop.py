# GCD using loop.

n1= int(input("Give first number: "))
n2= int(input("Give second number: "))

gcd = 1

for i in range (min(n1,n2)+1,0,-1):
    if(n1 % i == 0 and n2 % i ==0):
        print(i)
        break

    
    


