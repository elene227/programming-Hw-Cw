def digital_root(n):
    while n >= 10:
        digit = 0
        for i in str(n):
            digit += int(i)
        n = digit
    return n