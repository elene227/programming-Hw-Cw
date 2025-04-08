def bigger_number():
    num1 = float(input("შეიყვანეთ პირველი რიცხვი: "))
    num2 = float(input("შეიყვანეთ მეორე რიცხვი: "))
    if num1 > num2:
        print(f"დიდი რიცხვია: {num1}")
    elif num2 > num1:
        print(f"დიდი რიცხვია: {num2}")
    else:
        print("რიცხვები თანაბარია")
