def count_letters_and_digits(s):
    c = 0
    ch = "QWERTYUIOPASDFGHJKLZXCVBNMabcdefghijklmnopqrstuvwxyz1234567890"
    for i in s:
        if i in ch:
            c += 1
    return c
        