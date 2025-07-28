
def add (a, b):
    return a + b

def subtract (a, b):
    return a - b

def multiply (a, b):
    return a * b

def divide (a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b


def odd (a):
    return a % 2 != 0
def even (a):
    return a % 2 == 0