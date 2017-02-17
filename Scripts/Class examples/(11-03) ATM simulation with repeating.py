# this holds the user's current balance
balance = 1.90

repeat = 1
while repeat == 1:
    # show main menu
    print("Welcome to the totally legit ATM")
    print("1. Check balance")
    print("2. Deposit money")
    print("3. Withdraw money")


    # get user input for which choice s/he wants to make
    choice = int(input("Enter the number of your choice: "))

    if choice == 1:     # check balance
        print("Your current balance is: $" + str(round(balance,2)))
    elif choice == 2:   # deposit money
        depositAmt = float(input("How much do you want to deposit? "))
        balance = balance + depositAmt
        print("Your new balance is: $" + str(balance))
    elif choice == 3:   # withdraw money
        withdrawAmt = float(input("How much do you want to withdraw? "))
        # check for valid withdraw amount (must be positive, and no more than existing balance)
        if withdrawAmt <= balance and withdrawAmt > 0:
            balance = balance - withdrawAmt
            print("Your new balance is: $" + str(balance))
        else:
            print("Error, your balance is only $" + str(balance))

    # determine if user wants to repeat the program
    repeat = int(input("Do you want to repeat the program? (1 = yes) "))
    
print("Thank you, come again!")
