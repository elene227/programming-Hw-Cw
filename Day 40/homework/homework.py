def basic_op(operator, value1, value2):
    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1 - value2
    elif operator == '*':
        return value1 * value2
    elif operator == '/':
        if value2 != 0:
            return value1 / value2
        else:
            return "Error: Division by zero"
    else:
        return "Invalid operation"
