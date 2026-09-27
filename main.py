
# Student Grade Calculator

print("===== Student Grade Calculator =====")

name = input("Enter student name: ")

marks = []

for i in range(1, 6):
    mark = float(input(f"Enter marks for subject {i}: "))

    while mark < 0 or mark > 100:
        print("Please enter marks between 0 and 100.")
        mark = float(input(f"Enter marks for subject {i}: "))

    marks.append(mark)

total = sum(marks)
average = total / len(marks)

if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 40:
    grade = "D"
else:
    grade = "F"

print("\n===== Student Result =====")
print("Name:", name)
print("Total Marks:", total, "/ 500")
print("Average:", round(average, 2), "%")
print("Grade:", grade)

if average >= 40:
    print("Result: PASS")
else:
    print("Result: FAIL")