n = int(input("How many grades do you want to find the max from? "))

maxGrade = 0
i = 0
while i < n:
    nextGrade = float(input("What's the next grade? "))
    if nextGrade > maxGrade:
        maxGrade = nextGrade
    i = i + 1

print("The max grade is: " + str(maxGrade))
