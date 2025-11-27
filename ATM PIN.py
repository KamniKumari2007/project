balance = 5000
pin = 1234

print(" ATM Machine ")
user_pin = int(input("Enter PIN: "))

if user_pin == pin:
    print("1. Check Balance")
    print("2. Withdraw")
    print("3. Deposit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        print("Balance:", balance)

    elif choice == 2:
        amt = int(input("Enter amount: "))
        if amt <= balance:
            balance -= amt
            print("New Balance:", balance)
        else:
            print("Insufficient balance")

    elif choice == 3:
        amt = int(input("Enter amount: "))
        balance += amt
        print("New Balance:", balance)

else:
    print("Incorrect PIN")
