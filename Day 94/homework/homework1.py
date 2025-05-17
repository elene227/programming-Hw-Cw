def to_jaden_case(string):
    words = string.split()
    
    caps = ''
    
    for i in words:
        first = i[0].upper()
        rest = i[1:].lower()
        
        caps += first + rest + ' '
    return caps[:-1]
    