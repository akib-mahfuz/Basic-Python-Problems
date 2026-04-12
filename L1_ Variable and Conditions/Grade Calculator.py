# Grade Calculator – Assign grade based on marks.
# Mark: 0-32 = Fail, 33-60 = "C", 61-70 = "B", 71-80 = "A", 81-100 = "A+"

mark = int(input("Give your mark: "))
if mark < 32:
    Grade = "Fail"
elif mark >= 33 and mark <= 60:
    Grade = "C"
elif mark >= 61 and mark <= 70:
    Grade = "B"
elif mark >= 71 and mark <= 80:
    Grade = "A"
elif mark >= 81 and mark <= 100:
    Grade = "A+"

print(f"Your grade is {Grade}")
