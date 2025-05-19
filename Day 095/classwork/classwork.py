def encode(st):
    vowels = "aeiou"
    nums = "12345"
    res = ""
    for i in st: 
        zero = False 
        for c in range(len(vowels)): 
             if i == vowels[c]: 
                res += nums[c] 
                zero = True 
                break 
        if not zero: 
            res += i 
    return res 
def decode(st):
    nums = "12345"
    vowels = "aeiou"
    res = ""
    for i in st:
        zero = False
        for c in range(len(nums)):
            if i == nums[c]:
                res += vowels[c]
                zero = True
                break
        if not zero:
            res += i
    return res