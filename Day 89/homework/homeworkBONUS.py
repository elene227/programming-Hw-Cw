def highest_rank(arr):
    tie = arr[0]
    max = arr.count(tie)
    
    for i in arr:
        if arr.count(i) > max or arr.count(i) == max and tie < i:
            max = arr.count(i)
            tie = i
    return tie
    