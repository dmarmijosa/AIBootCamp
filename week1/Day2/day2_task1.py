#write a program to calculate the factorial of a number using a while loop
num = int(input("Enter a number to calculate its factorial: "))
factorial = 1
while num > 1:
    factorial *= num
    print(f"Current factorial value: {factorial} (after multiplying by {num})")
    num -= 1
print(f"The factorial is: {factorial}")