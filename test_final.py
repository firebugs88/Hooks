def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

class Calculator:
    def __init__(self):
        self.history = []
    
    def calculate(self, operation, a, b):
        if operation == "add":
            result = add_numbers(a, b)
        elif operation == "subtract":
            result = subtract_numbers(a, b)
        else:
            raise ValueError("Invalid operation")
        
        self.history.append(result)
        return result