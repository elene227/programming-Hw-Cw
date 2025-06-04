def alphabet_position(text):
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    res = ""
    text = text.lower()
    for i in text:
        if i in alphabet:
            res += str(alphabet.index(i)+ 1) + " "

        
    return res[:-1]
        
