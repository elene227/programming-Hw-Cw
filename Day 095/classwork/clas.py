num = 942
while num >= 942:
    digit = 0
    for i in str(num):
        digit += int(i)
    num = digit
print(num)