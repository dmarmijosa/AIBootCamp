# #example a simple import in Python whit alias
# import math as m
# print(m.sqrt(16))  # Imprime la raíz cuadrada de 16

#example of a simple import in Python
# from math import sqrt
# print(sqrt(16))  # Imprime la raíz cuadrada de 16

#Example of a simple function in Python
# def add_number(a,b):
#     return a + b
# number1 = int(input("Ingrese el primer número: "))
# number2 = int(input("Ingrese el segundo número: "))
# print(f"La suma de {number1} y {number2} es: {add_number(number1, number2)}")

#local Scope
# def greet():
#     message = "Hello, World!"  # Local variable
#     print(message)
# greet()

#global Scope
# greeting = "Hi"

# def say_hello():
#     greeting = "Hello, World!"  # Local variable
#     print(greeting)  # Accessing local variable
# say_hello()
# print(greeting)  # Accessing global variable outside the function