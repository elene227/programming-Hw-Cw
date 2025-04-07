# მომხმარებლისგან რიცხვის მიღება
number = int(input("შემოიტანეთ რიცხვი: "))

# რიცხვის გადამოწმება არის თუ არა ლუწი თუ კენტი whattever the hell it is
if number % 2 == 0:
    print(f"{number} არის ლუწი.")
else:
    print(f"{number} არის კენტი.")
