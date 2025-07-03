#21) გააკეთეთ კალკულატორი, სადაც მომხმარებელმა უნდა აირჩიოს რომელი მოქმედება უნდა (+, -, *, /) და შემოიტანოს ორი რიცხვი. შემდეგ კი დაპრინტეთ შედეგი.

num1 = int(input("please enter number: "))
num2 = int(input("please enter number: "))
symbol = input("enter operation: ")

if symbol == "+":
    print (num1 + num2)
elif symbol == "-":
    print(num1 - num2)
elif symbol == "*":
    print(num1 * num2)
elif symbol == "/":
    print(num1 / num2)
else:
    print("ERRROR")

