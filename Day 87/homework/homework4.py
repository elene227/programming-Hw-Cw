def string_clean(s):
    nums = '0123456789'
    res = ""
    for char in s:
        if not(char >= '0' and char <= '9'):
             res += char
    return res
        
        