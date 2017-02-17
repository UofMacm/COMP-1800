# This function returns the cost of a pizza with the specified
#  size and number of toppings
def pizzaCost(t, size):
    basePrice = 0
    pricePerTopping = 0
    
    if size == "M":
        basePrice = 11
        pricePerTopping = 1.99
    elif size == "L":
        basePrice = 15
        pricePerTopping = 2.99
    elif size == "XL":
        basePrice = 17.50
        pricePerTopping = 3.99
    elif size == "Mega":
        basePrice = 29.95
        pricePerTopping = 7.99
        
    cost = basePrice + t*pricePerTopping
    return cost

# The program starts running here!
numToppings = int(input("How many toppings? "))
size = input("What size? ")

print(round(pizzaCost(numToppings, size), 2))
