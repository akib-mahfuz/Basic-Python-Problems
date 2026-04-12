# Triangle Type – Equilateral, isosceles, scalene.

a, b, c = map(int, input("Enter three angles of triangle: ").split())
if a + b + c == 180:
    if a == b == c:
        print("Equilateral Triangle")
    elif a == b or b == c or c == a:
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")
else:
    print("Not A Triangle")
