# get user input for age
age = int(input("How old are you? Answer truthfully, please... "))

if age >= 18 and age <= 30:       # user is in range
    print("Come on in!")
elif age < 18:               # user is NOT old enough
    diff = 18 - age # how long does the user need to wait before being able to enter?
    if diff == 1:
        print("Come back in 1 year!")
    else:
        print("Come back in " + str(diff) + " years!")
elif age > 30:
    print("Why don't you go home and \"try\" to figure out how to Netflix and chill!")

# this part is outside any if statement, so it will always run
print("Thanks for using the Robo Bouncer!")
