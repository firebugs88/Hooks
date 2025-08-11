def add_numbers(a, b):
    """Add two numbers and return the result."""
    return a + b

def multiply_numbers(a, b):
    """Multiply two numbers and return the result."""
    return a * b

class Calculator:
    """A simple calculator class."""
    
    def __init__(self):
        self.history = []
    
    def calculate(self, operation, a, b):
        """Perform a calculation and store in history."""
        if operation == "add":
            result = add_numbers(a, b)
        elif operation == "multiply":
            result = multiply_numbers(a, b)
        else:
            result = None
        
        if result is not None:
            self.history.append(f"{operation}({a}, {b}) = {result}")
        
        return result