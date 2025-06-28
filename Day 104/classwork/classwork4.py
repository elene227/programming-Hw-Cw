def difference_of_squares(n):
    nums = 0
    squares = 0
    
    for i in range(1, n + 1):
        nums += i
        squares += i * i
    
    return nums ** 2 - squares