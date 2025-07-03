def find_outlier(integers):
    is_even = sum(1 for x in integers[:3] if x % 2 == 0) > 1

    for num in integers:
        if (num % 2 == 0) != is_even:
            return num