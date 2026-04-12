# Discount Calculator – Apply discount based on price range.
# Price: 1000-2000 = 5%, 2001-4000 = 10% and above 4000 = 15% discount

price = int(input("Enter price of product: "))
if 1000 <= price:
    if 1000 <= price <= 2000:
        discount_Rate = "5%"
        discout_AMT = price * 0.05
    elif 2001 < price <= 4000:
        discount_Rate = "10%"
        discout_AMT = price * 0.1
    elif price > 4000:
        discount_Rate = "15%"
        discout_AMT = price * 0.15

    print(f"After {discount_Rate} discount rate, net price is {price-discout_AMT} Taka")


else:
    print("Discount not available")
