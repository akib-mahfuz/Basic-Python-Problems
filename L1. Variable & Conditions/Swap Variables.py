# Swap values with temp variable
"""
a = 5
b = 6
print(f"Value of a = {a} & b = {b}")

temp = a
a = b
b = temp
print(f"After Swaping value, a = {a} & b = {b}")
"""
# Swap value without temp variables
a = 5
b = 6
print(f"Value of a = {a} & b = {b}")

a, b = b, a
print(f"After Swaping value, a = {a} & b = {b}")
