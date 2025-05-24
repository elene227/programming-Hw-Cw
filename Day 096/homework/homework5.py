def delete_nth(order,max_e):
    new = []
    
    for i in order:
        if new.count(i) < max_e:
            new.append(i)   
    
    return new 
            