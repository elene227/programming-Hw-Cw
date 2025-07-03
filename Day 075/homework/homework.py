def bonus_time(salary, bonus):
    total = salary * 10 if bonus else salary
    return "$" + str(total)
