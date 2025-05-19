while True:
    name = input("შეიყვანეთ თქვენი სახელი (თუ გსურთ გამოსვლა, შეიყვანეთ 'quit'): ")
    if name.lower() == "quit":
        break
    print(f"თქვენი სახელი არის {name}")
