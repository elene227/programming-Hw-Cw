sum_of_multiples_of_5 = 0

for i in range(1, 101):
    if i % 5 == 0:
        sum_of_multiples_of_5 += i
    else:
        pass

print(sum_of_multiples_of_5)
