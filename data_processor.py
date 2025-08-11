def filter_data(data, condition):
    return [item for item in data if condition(item)]

def sort_data(data, key_func=None, reverse=False):
    return sorted(data, key=key_func, reverse=reverse)

def aggregate_data(data, group_key, agg_func):
    groups = {}
    for item in data:
        key = group_key(item)
        if key not in groups:
            groups[key] = []
        groups[key].append(item)
    
    return {k: agg_func(v) for k, v in groups.items()}

class DataAnalyzer:
    def __init__(self):
        self.results = {}
    
    def analyze(self, dataset, operations):
        for op_name, operation in operations.items():
            self.results[op_name] = operation(dataset)
        return self.results