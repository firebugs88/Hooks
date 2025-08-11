def reverse_string(text):
    return text[::-1]

def capitalize_words(text):
    return text.title()

def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

class StringFormatter:
    def __init__(self, prefix="", suffix=""):
        self.prefix = prefix
        self.suffix = suffix
    
    def format_text(self, text):
        return f"{self.prefix}{text}{self.suffix}"