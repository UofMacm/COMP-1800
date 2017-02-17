# This program uses Newton's method to find the square root of
#  a number.

n = float(input("Enter number to find the sqrt of: "))
x = float(input("Enter an initial estimate: "))

while x != (x + n/x)/2: # while the estimate is still changing...
    print("Current estimate = " + str(x))
    x = (x + n/x)/2

print("Final estimate = " + str(x))
