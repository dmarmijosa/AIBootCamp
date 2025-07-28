import math_operators as math_ops

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Addition:", math_ops.add(num1, num2))
print("Subtraction:", math_ops.subtract(num1, num2))
print("Multiplication:", math_ops.multiply(num1, num2))
print("Division:", math_ops.divide(num1, num2))

print("Is first number odd?", math_ops.odd(num1))
print("Is second number even?", math_ops.even(num2))