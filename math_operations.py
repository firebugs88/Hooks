def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

class MathProcessor:
    def __init__(self):
        self.operations = []
    
    def process(self, operation, a, b):
        if operation == "multiply":
            result = multiply(a, b)
        elif operation == "divide":
            result = divide(a, b)
        else:
            raise ValueError("Unsupported operation")
        
        self.operations.append((operation, a, b, result))
        return result