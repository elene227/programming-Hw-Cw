def arr_check(arr):
    if not arr and arr == {}:
        return False
    
    for D in arr:
        if type(D) != list:
            return False
        

    return True #(((((: YAYYY!! it worked ><!!!