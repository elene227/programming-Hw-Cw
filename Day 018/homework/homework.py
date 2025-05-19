# Starting balance
balance = 1000

def check_balance():
    print("Your current balance is: $" + str(balance))

def deposit():
    amount = float(input("Enter amount to deposit: $"))
    if amount > 0:
        global balance
        balance += amount
        print("Deposited $" + str(amount) + ". Your new balance is $" + str(balance))
    else:
        print("Please enter a valid amount.")

def withdraw():
    amount = float(input("Enter amount to withdraw: $"))
    if amount <= 0:
        print("Please enter a valid amount.")
    elif amount > balance:
        print("Insufficient balance.")
    else:
        global balance
        balance -= amount
        print("Withdrew $" + str(amount) + ". Your new balance is $" + str(balance))

def display_menu():
    print("Welcome to the Bank!")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

while True:
    display_menu()
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        check_balance()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        print("Thank you for using the bank. Goodbye!")
        break
    else:
        print("Invalid option, please try again.")

