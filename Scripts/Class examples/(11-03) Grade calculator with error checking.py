# get user input for the numerical grade
##grade = float(input("Enter your numerical grade: "))
##while grade < 0 or grade > 100:
##    print("Sorry, the grade must be between 0-100!")
##    grade = float(input("Enter your numerical grade: "))

grade = -1
while grade < 0 or grade > 100:
    grade = float(input("Enter your numerical grade: "))
    if grade < 0 or grade > 100:
        print("Sorry, the grade must be between 0-100!")

# determine the corresponding letter grade
if grade >= 90:
    print("You have an A!")
elif grade >= 80:
    print("You have a B!")
elif grade >= 70:
    print("You have a C!")
elif grade >= 60:
    print("You have a D!")
elif grade >= 0:
    print("You have an F! :(")
