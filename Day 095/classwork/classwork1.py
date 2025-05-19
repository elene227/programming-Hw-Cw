def spin_words(sentence):
    sentence = sentence.split()
    rev = ''
    
    for i in (sentence):
        if len(i) >= 5:
            ras = ""
            for c in i:
                ras = c + ras
            rev += ras + " "
        else:
            rev += i + " "
    return rev[:-1]
                
            
       
