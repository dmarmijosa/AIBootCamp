#Menu calculator
# This code is a simple calculator that performs addition, subtraction, multiplication, and division.
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero is not allowed."
while True:
    print("Menu:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")
    if choice == '5':
        print("Exiting the calculator. Goodbye!")
        break
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == '1':
        print(f"The result of {num1} + {num2} is: {add(num1, num2)}")
    elif choice == '2':
        print(f"The result of {num1} - {num2} is: {subtract(num1, num2)}")

    elif choice == '3':
        print(f"The result of {num1} * {num2} is: {multiply(num1, num2)}")

    elif choice == '4':
        print(f"The result of {num1} / {num2} is: {divide(num1, num2)}")
    else:
        print("Invalid choice. Please try again.")
    print()  # Print a newline for better readability
# End of calculator code
