def count_zeros(x):
    res = 0
    for i in range(10, x + 1):
        if '0' in str(i):
            res += str(i).count('0')
    return res
            