def compute_sum(n):
    su = 0
    for i in range(1, n + 1):
        if i >= 10:
            for c in str(i):
                su += int(c)
        else:
            su += i
    return su
    