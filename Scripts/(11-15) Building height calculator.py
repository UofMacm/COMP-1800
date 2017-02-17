# This program computes the height of a building, given
#  the angle measure to the top and the horizontal distance
#  to the building's base.

import math

theta = float(input("Enter the angle measure to the top of the building (in degrees): "))
d = float(input("Enter the horizontal distance to the base of the building (in feet): "))

# convert theta from degrees into radians
# (since Python expects arguments to the tan function to be expressed in radians)
theta = theta*math.pi/180

# tan(theta) = h/d, so d = h*tan(theta)
h = d*math.tan(theta)

print("Your building is this tall: " + str(h) + " feet")
