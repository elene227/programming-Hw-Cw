def enough(cap, on, wait):
    sits_rem = cap - on
    
    if sits_rem >= wait:
        return 0
    else:
        return wait - sits_rem

print(enough(10, 5, 5))  
print(enough(100, 60, 50))  

