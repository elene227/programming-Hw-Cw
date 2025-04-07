sum_of_multiples_of_5 = 0

for i in range(1, 101):
    if i % 5 == 0:
        sum_of_multiples_of_5 += i
    else:
        continue

print("ხუთის ჯერადი რიცხვების ჯამი 1-დან 100-მდე:", sum_of_multiples_of_5)
