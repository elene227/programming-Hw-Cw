def disemvowel(string_):
    vowels = "aeiouAEIOU"
    res = ''
    for i in string_:
        if i not in vowels:
            res += i
    return res