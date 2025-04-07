def calculate_age(birth, current):
    m = current - birth
    
    if m == 0:
        return("You were born this very year!")
    elif m > 1:
        return "You are " + str(m) + " years old."
    elif m == 1:
        return "You are 1 year old."
    elif m == -1:
        return "You will be born in 1 year."
    else:
        return "You will be born in " + str(m * -1) + " years."