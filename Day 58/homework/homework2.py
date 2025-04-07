def get_participants(handshakes):
    n = 2
    while (n * (n - 1)) // 2 < handshakes:
        n += 1
    if (n * (n - 1)) // 2 == handshakes:
        return n
    else:
        return -1
