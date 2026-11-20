
# Basic Python Programs
# Variables, Operators, Input and Output

# Taking input from the user
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Displaying output
print("\nStudent Information")
print("Name:", name)
print("Age:", age)

# Taking two numbers
a = float(input("\nEnter first number: "))
b = float(input("Enter second number: "))

# Arithmetic operators
print("\nArithmetic Operations")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)

if b != 0:
    print("Division:", a / b)
    print("Floor Division:", a // b)
    print("Modulus:", a % b)
else:
    print("Division by zero is not possible.")

print("Exponent:", a ** b)

# Comparison operators
print("\nComparison Operations")
print("a is greater than b:", a > b)
print("a is equal to b:", a == b)
print("a is less than b:", a < b)

# Logical operator
print("\nLogical Operation")
print("Both numbers are positive:", a > 0 and b > 0)
