# შექმენით ფუნქცია რომელიც გამოითვლის სიაში მყოფი ელემენტების ჯამს
def sum(nums):
    first = 0
    for i in nums:
        first += i
    return first

print(sum([5,6,5,6,7,8]))

