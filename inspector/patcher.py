# inspector/patcher.py

def patch_function(module, func_name, new_func):
    setattr(module, func_name, new_func)