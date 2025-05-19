def solution(s):
    res = ''
    for c in s:
        if 'A' <= c <= 'Z':  
            res += ' ' + c
        else:
            res += c
    return res