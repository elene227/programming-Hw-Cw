def generate_hashtag(s):
    if s == "":
        return False
    
    by = s.split()
    
    if len(by) == 0:
        return False
    
    res = '#'
    for i in by:
        cap = i[0].upper() + i[1:].lower()
        res += cap 
        
    if len(res) > 140:
        return False
    return res
        
def generate_hashtag(s):
    has = ""
    s = s.split()
    for i in s:
        has += i.capitalize()
    if len(has) >= 140 or has == "":
        return False
    return "#" + has
        
            
            
        
    
    
    
    
    
        
       