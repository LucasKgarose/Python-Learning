# inspector/meta.py

import inspect

def inspect_module(module):
    functions = inspect.getmembers(module, inspect.isfunction)
    
    info = []
    for name, func in functions:
        info.append({
            "name": name,
            "doc": inspect.getdoc(func),
            "args": str(inspect.signature(func))
        })
    
    return info