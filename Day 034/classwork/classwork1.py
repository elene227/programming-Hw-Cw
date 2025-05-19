def check_even_odd():
    number = int(input("შეიყვანე რიცხვი: "))
    if number % 2 == 0:
        print(f"{number} არის ლუწი.")
    else:
        print(f"{number} არის კენტი.")

check_even_odd()