def sum_of_minimums(numbers):
    total = 0
    
    for i in numbers:
        val = min(i)
        
        total += val
    return total