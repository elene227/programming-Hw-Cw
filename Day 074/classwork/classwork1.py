# input is an unsorted list of 3 positive integers
def pythagorean_triple(integers):
    integers.sort()
    return integers[0]**2 + integers[1]**2 == integers[2]**2


