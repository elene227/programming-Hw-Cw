def duplicate_encode(word):
    word = word.lower()
    res = ""
    for i in range(len(word)):
        e = word[i]
        count = 0
        for l in range(len(word)):
            if word[l] == e:
                count = count + 1
        if count == 1:
            res = res + "("
        else:
            res = res + ")"
    return res
    
        
