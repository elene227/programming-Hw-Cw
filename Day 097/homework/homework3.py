def nickname_generator(name):

    if len(name) < 4:
        return "Error: Name too short"
    vowels = "aeiou"
    
    
    if name[2].lower() in vowels:
        return name[:4]  
    else:
        return name[:3]