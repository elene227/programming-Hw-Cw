def is_opposite(s1,s2):
    if s1 == "" and s2 == "":
        return False
    elif s1.lower() == s2.lower():
        for i in range(len(s1)):
            if s1[i] == s2[i]:
                return False
    return True
                
   
def is_opposite(s1,s2):
    if s1 == "" or s2 == "":
        return False
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            return False
    return True
        