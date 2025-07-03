def move_zeros(lst):
    ind = 0
    
    for num in lst:
        if num != 0:
            lst[ind] = num
            ind += 1
            
    while ind < len(lst):
        lst[ind] = 0
        ind += 1
    return lst