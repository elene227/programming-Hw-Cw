def to_camel_case(text):
    text = text.replace("_","-")
    split = text.split("-")
    
    res = [split[0]]
    
    for elem in split[1:]:
        res.append(elem.capitalize())
        
    return "".join(res)