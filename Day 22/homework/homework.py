def register_user():
    existing_usernames = ["user123", "admin", "guest"]
    
    while True:
        username = input("მიუთითეთ თქვენი მომხმარებლის სახელი (3-15 სიმბოლო): ")
        
        if len(username) < 3 or len(username) > 15:
            print("სახელი უნდა იყოს 3-15 სიმბოლო.")
            continue
        
        if username in existing_usernames:
            print(f"მომხმარებლის სახელი '{username}' უკვე არსებობს. გთხოვთ, გამოიყენოთ სხვა.")
            continue

        email = input("მიუთითეთ თქვენი ელ.ფოსტა: ")
        
        if "@" not in email or "." not in email:
            print("არასწორი ელ.ფოსტა. გთხოვთ, შეიყვანოთ სწორი ელ.ფოსტა.")
            continue

        password = input("მიუთითეთ პაროლი (მინიმუმ 8 სიმბოლო, ციფრები და ასოები): ")
        
        if len(password) < 8:
            print("პაროლი უნდა იყოს მინიმუმ 8 სიმბოლო.")
            continue
        
        if not any(char.isdigit() for char in password) or not any(char.isalpha() for char in password):
            print("პაროლი უნდა შეიცავდეს ციფრებს და ასოებს.")
            continue

        confirm_password = input("გაიმეორეთ პაროლი: ")
        
        if password != confirm_password:
            print("პაროლები არ ემთხვევა. გთხოვთ, სცადეთ კიდევ.")
            continue
        
        print("რეგისტრაცია წარმატებით დასრულდა!")
        existing_usernames.append(username)
        break

    print("რეგისტრირებული მომხმარებლები:")
    for user in existing_usernames:
        print(user)

register_user()
