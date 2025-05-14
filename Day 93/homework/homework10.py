def narcissistic( value ):
    val = 0
    for i in str(value):
         val += int(i) ** len(str(value))
    return val == value