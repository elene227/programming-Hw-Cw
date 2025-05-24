def pig_it(text):
    
    words = text.split()
    
   
    transformed_words = []
    
    for word in words:
       
        if word.isalpha():
            
            transformed_word = word[1:] + word[0] + 'ay'
        else:
            
            transformed_word = word
        
       
        transformed_words.append(transformed_word)
    
   
    return ' '.join(transformed_words)
