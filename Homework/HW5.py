# getDistance function - Finds travel distance from one corner to another
def getDistance(s1,a1,s2,a2):
    sDelta = abs(s1 - s2)
    aDelta = abs(a1 - a2)
    distance = (sDelta*500)+(aDelta*500)
    return distance
# Test code for getDistance
#s1 = int(input("What is the starting street? "))
#a1 = int(input("What is the starting avenue? "))
#s2 = int(input("What is the ending street? "))
#a2 = int(input("What is the ending avenue? "))
#print(getDistance(s1,a1,s2,a2))


# ordinal function - Ordinates the numbers
def ordinal(n):
    if n == 11 or n == 12 or n == 13:
        ordNum = str(n) + "th"
    elif n%10 == 1:
        ordNum = str(n) + "st"
    elif n%10 == 2:
        ordNum = str(n) + "nd"
    elif n%10 == 3:
        ordNum = str(n) + "rd"
    else:
        ordNum = str(n) + "th"
    return ordNum

# Test code for ordinal
#n = int(input("What number should I ordinate? "))
#print(ordinal(n))

# getDirections function - A very poor imiation of Google Maps
def getDirections(s1,a1,s2,a2):
    # Gets the North/South direction
    if a1<a2:
        nscard = "North"
    elif a1>a2:
        nscard = "South"
    # Gets the East/West direction
    if s1<s2:
        wecard = "West"
    elif s1>s2:
        wecard = "East"

    # Gets turn information based on cardinal dirction and avenue and street names
    if wecard == "West" and a2>a1:
        turn = "left"
    elif wecard == "West" and a2<a1:
        turn = "right"
    elif wecard == "East" and a2<a1:
        turn = "left"
    elif wecard == "East" and a2>a1:
        turn = "right"

    # Calculates distance
    aDelta = abs(a1 - a2)
    sDelta = abs(s1 - s2)

    aDist = aDelta*500
    sDist = sDelta*500

    # print time
    print("Directions from "+ ordinal(s1) +" and "+ ordinal(a1) +" to "+ ordinal(s2) +" and "+ ordinal(a2) +":\n")
    print("Take "+ ordinal(a1) + " Ave. "+ wecard +" for "+str(aDist)+" ft until you get to "+ ordinal(s2) +" St.")
    print("Turn "+ turn +" onto "+ ordinal(s2) +" St.")
    print("Take "+ ordinal(s2) + " St. "+ nscard +" for "+str(sDist)+" ft until you get to "+ ordinal(a2) +" Ave.")

    return ("You have arrived at your destination!");

# Test code for getDirections
#s1 = int(input("What is the starting street? "))
#a1 = int(input("What is the starting avenue? "))
#s2 = int(input("What is the ending street? "))
#a2 = int(input("What is the ending avenue? "))
#print(getDirections(s1,a1,s2,a2))

print("Welcome to XMaps! We get you where you need to go!")
i = 1
while i == 1:
    s1 = 2
    while s1%2 == 0 or s1 < 1 or s1 > 99:
        s1 = int(input("Starting street: "))
        if s1%2 == 0 or s1 < 1 or s1 > 99:
            print("That is not a vaild street number. Try again!")

    a1 = 1
    while a1%2 == 1 or a1 < 2 or a1 > 98:
        a1 = int(input("Starting avenue: "))
        if a1%2 == 1:
            print("That is not a vaild avenue number. Try again!")

    s2 = 2
    while s2%2 == 0 or s2 < 1 or s2 > 99:
        s2 = int(input("Ending street: "))
        if s2%2 == 0:
            print("That is not a vaild street number. Try again!")

    a2 = 1
    while a2%2 == 1 or a2 < 2 or a2 > 98:
        a2 = int(input("Starting avenue: "))
        if a2%2 == 1:
            print("That is not a vaild avenue number. Try again!")

    print(getDirections(s1,a1,s2,a2) + "\n\nTotal distance traveled: " + str(getDistance(s1,a1,s2,a2)) + " ft.\n")
    i = int(input("Enter 1 to get more directions, any other key to exit..."))
print("Thank you for using XMaps!")
