def calculator(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Invalid operator"

def find_max(numbers):
    return max(numbers)

def find_min(numbers):
    return min(numbers)

def letter_position(name):
    first_letter = name[0].upper()
    position = ord(first_letter) - ord('A') + 1
    return position

def greet():
    print("Hello! How are you today?")
