correct_password = "password123"
password = input("შეიყვანეთ პაროლი: ")
while password != correct_password:
    password = input("პაროლი არასწორია, სცადეთ კიდევ: ")
print("ექაუნთზე შესვლა წარმატებით განხორციელდა.")