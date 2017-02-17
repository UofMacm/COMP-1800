# This program computes the final price of a pizza order.
# Our store sells only three types of items:
#  pizzas for $15 each
#  side items for $7.50 each
#  drinks for $4.99 each
repeat = "yes"
while repeat == "yes":
    # get user input
    numPizzas = int(input("How many pizzas do you want? "))
    while numPizzas < 0:
        print("Sorry! We don't want you to make us a pizza. We have enough already.")
        numPizzas = int(input("How many pizzas do you want? "))
    numSides = int(input("How many sides do you want? "))
    while numSides < 0:
        print("Sorry! We don't want you to make us any sides. We have enough already.")
        numSides = int(input("How many sides do you want? "))
    numDrinks = int(input("How many drinks do you want? "))
    while numDrinks <0:
        print("Sorry! We don't want you to make us any drinks. We have our own.")
        numDrinks = int(input("How many drinks do you want? "))

    # do some calculations
    subtotal = 15*numPizzas + 7.5*numSides + 4.99*numDrinks
    tax = 0.0925*subtotal
    total = subtotal + tax

    # show the results
    print("Subtotal = $" + str(round(subtotal, 2)))
    print("Tax =      $" + str(round(tax, 2)))
    print("Total =    $" + str(round(total, 2)))
    print("  T H A N K   Y O U !!!!!!!!!")
    repeat = input("Do you have another order? ")
