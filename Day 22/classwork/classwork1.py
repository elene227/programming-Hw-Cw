num = int(input("შეიყვანეთ რიცხვი: "))
i = 1
while i <= num:
    if i % 2 == 0:
        print(f"{i} - ლუწი")
    else:
        print(f"{i} - კენტი")
    i += 1
