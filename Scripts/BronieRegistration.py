ssn = input("Welcome to BronieNation! Please enter your Social Security Number to continue...")
while len(ssn) != 9:
    print("Please enter a vaild Social Security Number to continue...")
    ssn = input("Welcome to BronieNation! Please enter your Social Security Number to continue...")
    while ssn.startswith("0"):
        print("Please enter a vaild Social Security Number to continue...")
        ssn = input("Welcome to BronieNation! Please enter your Social Security Number to continue...")
print("Thank you! You are now registered on our forums.")
