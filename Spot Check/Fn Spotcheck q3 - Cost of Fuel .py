print("This Program:")
print("Calculates the fuel cost of your next journey")

#get values from user
def getValues():
    distance = input("Journey distance (in Miles): ")
    distance = float(distance)
    Mpg = input("Miles Per Gallon: ")
    Mpg = float(Mpg)
    p = input("Price of Petrol (In Pence): ")
    p = float(p)
    return distance, Mpg, p

def calculateCost(distance, Mpg, p):
    valid = False
    Mpg = Mpg / 4.55
    #fuel needed in litres
    fuelNeeded = Mpg * distance
    fuelCost = (fuelNeeded * p) / 100
    print(fuel)
##    if fuel =
    return fuelNeeded, fuelCost

##the test
def theCheck():
    valid = False
    while valid == False:
        cost = calculateCost(distance, Mpg, p)
        print(cost)
