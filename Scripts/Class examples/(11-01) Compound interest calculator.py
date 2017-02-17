# how much money you start with
initialAmt = float(input("Enter initial amount: "))

# how much money you contribute per month
monthlyExtra = float(input("Enter monthly contribution: "))

# annual interest rate, as a percentage
annualInterestRate = float(input("Enter annual interest rate (as a percentage): "))

# number of months to compute
numMonths = int(input("How many months? "))

startBalance = initialAmt   # balance at the beginning of month i
i = 1
while i <= numMonths:
    interestEarned = annualInterestRate/1200*startBalance       # interest earned during month i
    endBalance = startBalance + interestEarned + monthlyExtra   # balance at the end of month i
    print("Month " + str(i) + ":\t$" + str(round(startBalance, 2)) + "\t$" + str(round(interestEarned, 2)) + "\t$" + str(round(monthlyExtra, 2)) + "\t$" + str(round(endBalance, 2)))
    startBalance = endBalance   # the starting balance for the next month is the same as the ending balance of this month
    i = i + 1
