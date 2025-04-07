def minimum(arr):
    return min(arr)

def maximum(arr):
    return max(arr)


# harder solution

def minimum(arr):
    min = arr[0]
    
    for num in arr:
        if num < min:
            min = num
    return min 

def maximum(arr):
    max = arr[0]
    
    for num in arr:
        if num > max:
            max = num
    return max 