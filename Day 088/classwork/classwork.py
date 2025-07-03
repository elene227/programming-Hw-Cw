def sum_array(arr):
    if arr is None or len(arr) < 3:
        return 0

    total = 0
    highest = arr[0]
    lowest = arr[0]

    for num in arr:
        total += num
        if num > highest:
            highest = num
        if num < lowest:
            lowest = num

    return total - highest - lowest