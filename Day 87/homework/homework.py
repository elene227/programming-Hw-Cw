def get_drink_by_profession(param):
    param = param.lower()
    
    if param == "jabroni":
        return "Patron Tequila"
    elif param == "school counselor":
        return "Anything with Alcohol"
    elif param == "programmer":
        return "Hipster Craft Beer"
    elif param == "bike gang member":
        return "Moonshine"
    elif param == "politician":
        return "Your tax dollars"
    elif param == "rapper":
        return "Cristal"
    else:
        return "Beer"
