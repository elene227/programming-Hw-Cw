def is_isogram(string):
    string = string.lower()
    count = 0
    for i in string:
        if string.count(i) > 1:
            return False
    return True