n = int(input("შეიყვანეთ რიცხვი: "))

for i in range(1, n + 1):
    if i % 2 == 0:
        print(f"{i} ლუწია")
    else:
        print(f"{i} კენტია")
