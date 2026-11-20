
# CSV-Based Payroll Management System

import csv
import os

filename = "payroll.csv"

# Create CSV file if it does not exist

if not os.path.exists(filename):

    with open(filename, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            "Employee ID",
            "Name",
            "Basic Salary",
            "Allowance",
            "Deduction",
            "Net Salary"
        ])


while True:

    print("\n===== PAYROLL MANAGEMENT SYSTEM =====")

    print("1. Add Employee")
    print("2. Display Payroll")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        emp_id = input("Enter Employee ID: ")

        name = input("Enter Employee Name: ")

        basic = float(input("Enter Basic Salary: "))

        allowance = float(input("Enter Allowance: "))

        deduction = float(input("Enter Deduction: "))

        net_salary = basic + allowance - deduction

        with open(filename, "a", newline="") as file:

            writer = csv.writer(file)

            writer.writerow([
                emp_id,
                name,
                basic,
                allowance,
                deduction,
                net_salary
            ])

        print("Employee record saved successfully.")
        print("Net Salary:", net_salary)

    elif choice == "2":

        with open(filename, "r") as file:

            reader = csv.reader(file)

            for row in reader:

                print(row)

    elif choice == "3":

        print("Exiting Payroll System.")
        break

    else:

        print("Invalid choice.")
