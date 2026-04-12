# Triangle Validity – Check if 3 sides form a triangle.

a, b, c = map(int, input("Enter three sides of triangle: ").split())
if (a + b > c) and (b + c > a) and (c + a > b):
    print("Triangle is valid")
else:
    print("Triangle is not valid")
