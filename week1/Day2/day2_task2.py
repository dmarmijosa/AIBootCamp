#create a program to find the largest number in a list using a while loop
numbers = []
number = int(input("Enter number for the list:"))
numbers.append(number)
print("Current list of numbers:", numbers)

def addNumber():
    while True:
        number = int(input("Enter number for the list (0 to finish): "))
        if number == 0:
            break
        numbers.append(number)
        print("Current list of numbers:", numbers)

addNumber()

if numbers:
    largest = max(numbers)
    print(f"The largest number in the list is: {largest}")
else:
    print("No numbers were entered.")
