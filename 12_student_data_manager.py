
# Student Data Manager Using Files

import json
import os

filename = "students.json"

# Load student data from file

if os.path.exists(filename):

    with open(filename, "r") as file:
        students = json.load(file)

else:

    students = []


while True:

    print("\n===== STUDENT DATA MANAGER =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        roll = input("Enter roll number: ")

        name = input("Enter student name: ")

        course = input("Enter course: ")

        student = {
            "roll": roll,
            "name": name,
            "course": course
        }

        students.append(student)

        with open(filename, "w") as file:
            json.dump(students, file, indent=4)

        print("Student added successfully.")

    elif choice == "2":

        if len(students) == 0:
            print("No student records found.")

        else:

            for student in students:

                print("\nRoll Number:", student["roll"])
                print("Name:", student["name"])
                print("Course:", student["course"])

    elif choice == "3":

        roll = input("Enter roll number to search: ")

        found = False

        for student in students:

            if student["roll"] == roll:

                print("Student Found!")
                print(student)

                found = True
                break

        if not found:
            print("Student not found.")

    elif choice == "4":

        print("Exiting Student Data Manager.")
        break

    else:

        print("Invalid choice.")
