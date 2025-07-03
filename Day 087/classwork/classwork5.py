def solution(s):
    res = []
    
    if len(s) % 2 == 1:
        s += "_"
        
    for i in range(0, len(s), 2):
        pairs = s[i:i + 2]
        res.append(pairs)
    return res
        
        
    
    