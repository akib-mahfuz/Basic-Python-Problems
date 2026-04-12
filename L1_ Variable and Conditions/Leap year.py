# Check leap year.

# Solve 1
"""
year = int(input("Give year: "))
if (year % 4 == 0 and year % 100 != 0) or (year == 400):
    print(f"{year} is a leap year")

else:
    print(f"{year} is not a leap year")
"""

# Solve 2
year = int(input("Give year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
    else:
        print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
