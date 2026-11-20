
# Student Grading System

name = input("Enter student name: ")

number = int(input("Enter number of subjects: "))

marks = []

for i in range(number):

    mark = float(input("Enter marks for subject " + str(i + 1) + ": "))

    marks.append(mark)

total = sum(marks)

percentage = total / number

print("\n===== STUDENT RESULT =====")

print("Student Name:", name)
print("Total Marks:", total)
print("Percentage:", percentage)

if percentage >= 90:
    grade = "A+"

elif percentage >= 80:
    grade = "A"

elif percentage >= 70:
    grade = "B"

elif percentage >= 60:
    grade = "C"

elif percentage >= 50:
    grade = "D"

elif percentage >= 40:
    grade = "E"

else:
    grade = "F"

print("Grade:", grade)

if percentage >= 40:
    print("Result: PASS")

else:
    print("Result: FAIL")
