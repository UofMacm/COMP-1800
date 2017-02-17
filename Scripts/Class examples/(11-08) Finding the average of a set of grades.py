n = int(input("How many grades do you want to average? "))

sumGrades = 0
i = 0
while i < n:
    nextGrade = float(input("What's the next grade you want to average? "))
    sumGrades = sumGrades + nextGrade
    i = i + 1

average = sumGrades/n
print("The average is " + str(average))
