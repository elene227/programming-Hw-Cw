def small_enough(array, limit):
    for value in array: 
        if value > limit:  
            return False
    return True  
