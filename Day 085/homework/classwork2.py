def cal(num1, num2, opp):
    if opp == "+":
        result = num1 + num2
    elif opp == "-":
        result = num1 - num2
    elif opp == "*":
        result = num1 * num2
    elif opp == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            return "YOU CANT DO datt with zeroo >:("
    else:
        return "WRONG OPP"
    return f"{num1} {opp} {num2} = {result}"
print(cal(5, 6, '/'))
    