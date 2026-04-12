# Electricity Bill – Calculate bill with slabs.
# Electric Bill per unit:- 0-100 Unit: 4 tk/unit, next 101-200: 6 tk/unit, above 200: 8 tk/unit

usage = int(input("Enter electicity usage: "))
if usage < 0:
    print("Usage cann't be negative")
else:
    if usage <= 100:
        bill = 100 * 4
    elif usage <= 200:
        bill = 400 + (usage - 100) * 6
    else:
        bill = 1000 + (usage - 200) * 8
    print(f"Your eletricity bill is {bill}")
