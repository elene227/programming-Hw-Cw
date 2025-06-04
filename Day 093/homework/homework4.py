def dating_range(age):
    if age <= 14:
        min = int(age - 0.10 * age)
        max = int(age + 0.10 * age)
    else:
        min = int(age / 2 + 7)
        max = int((age - 7) * 2)
    return f"{min}-{max}"