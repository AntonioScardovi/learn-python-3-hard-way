def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLY {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDE {a} / {b}")
    return a / b

formula = divide(add(23, 34), subtract(100, 1023))
print(formula)
