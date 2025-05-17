def count_red_beads(n):
    count = 0
    if n <= 2:
        return 0
    elif n > 2:
        while n - 1:
            n -= 1
            count += 2
    return count