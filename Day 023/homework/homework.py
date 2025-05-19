for i in range(101):
    addition = i + 10
    subtraction = i - 5
    multiplication = i * 2
    if i != 0:
        division = i / 2
    else:
        division = "undefined"
    
    print(f"Number: {i}")
    print(f"Addition (i + 10): {addition}")
    print(f"Subtraction (i - 5): {subtraction}")
    print(f"Multiplication (i * 2): {multiplication}")
    print(f"Division (i / 2): {division}")
    print("-" * 30)
