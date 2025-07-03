def add_length(word):
    splited = word.split()
    result = []
    
    for w in splited:
        result.append(w + ' ' + str(len(w)))
    
    return result
