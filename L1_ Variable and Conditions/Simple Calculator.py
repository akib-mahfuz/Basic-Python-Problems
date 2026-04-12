# Simple Calculator (+, -, *, /)

num1, num2 = map(float, input("Give to numbers to calculate: ").split())
Operation = input("Choose operation (+, -, *, /)")

if Operation == "+":
    result = num1 + num2
elif Operation == "-":
    result = num1 - num2
elif Operation == "*":
    result = num1 * num2
elif Operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Values are not dividable by 0"
else:
    result = "Invalid Operation"

print("Result: ", result)
