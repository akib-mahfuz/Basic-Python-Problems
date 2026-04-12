# Profit or Loss – Calculate based on cost and selling price.

Sp = int(input("Enter your selling price: "))
cost = int(input("Enter cost of product: "))

if Sp - cost >= 0:
    print(f"Your profit is {Sp-cost} TK")
else:
    print(f"Your loss is {cost-Sp} TK")
