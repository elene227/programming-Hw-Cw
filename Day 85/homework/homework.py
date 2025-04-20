def addition(num):
    first = 0
    for i in num:
        first += i
    return first

yess = [5, 6, 5, 6, 7, 8]
another = [2, 4, 6, 8]

to = addition(yess + another)

print(f"the sum of this numss toghterr isss!! {to}")
