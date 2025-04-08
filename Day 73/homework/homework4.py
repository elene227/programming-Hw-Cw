def validate_hello(greetings):
    greetings_list = ["hello", "ciao", "salut", "hallo", "hola", "ahoj", "czesc"]
    
    greetings = greetings.lower()
    for greeting in greetings_list:
        if greeting in greetings:
            return True
    return False