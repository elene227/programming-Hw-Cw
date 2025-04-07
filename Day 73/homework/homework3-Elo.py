def validate_hello(greetings):
    
    hellos = ["hello", "ciao", "salut", "hallo", "hola", "ahoj", "czesc"]
     
    greetings = greetings.lower()
    
    for hello in hellos:
        if hello in hellos:
            return True 
        
        return False
    