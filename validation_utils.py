def validate_email(email):
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_phone(phone):
    import re
    pattern = r'^\+?1?-?\(?(\d{3})\)?[-.\s]?(\d{3})[-.\s]?(\d{4})$'
    return re.match(pattern, phone) is not None

def validate_url(url):
    import re
    pattern = r'^https?://(?:[-\w.])+(?::\d+)?(?:/(?:[\w/_.])*(?:\?(?:[\w&=%.])*)?(?:#(?:\w)*)?)?$'
    return re.match(pattern, url) is not None

class InputValidator:
    def __init__(self):
        self.rules = {}
    
    def add_rule(self, field, validator_func):
        self.rules[field] = validator_func
    
    def validate(self, data):
        results = {}
        for field, value in data.items():
            if field in self.rules:
                results[field] = self.rules[field](value)
            else:
                results[field] = True  # No validation rule, assume valid
        return results