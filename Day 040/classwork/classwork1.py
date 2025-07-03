def hello(name=""):
    if not name:
        return "Hello, World!"
    
    return f"Hello, {name.capitalize()}!"
