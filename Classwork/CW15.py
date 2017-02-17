import math

x = 0.0
while x <= 100.0:
    result = math.sin(x)**2 + math.cos(x)**2
    print("x = " + str(round(x,1)) + ": result = " + str(round(result,1)))
    x = x + 0.1
