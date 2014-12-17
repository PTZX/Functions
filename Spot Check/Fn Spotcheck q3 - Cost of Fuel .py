print("Calculates the cost of fuel of your next Journey")

def getValues():
    d = input("Journey Distance (in Miles): ")
    d = int(d)
    Mpg = input("Miles Per Gallon: ")
    Mpg = int(Mpg)
    p = input("Price of Petrol (In Pence): ")
    p = int(p)
    return d, Mpg, p

def CalculateCost(d, Mpg, p):
    Mpg = Mpg * 4.55
    #fuel needed in litres
    FuelNeeded  = Mpg * d
    FuelCost = (FuelNeeded  * p) / 100
    print(fuel)
    return FuelNeeded, FuelCost

def main():
    Cost = CalculateCost(FuelNeeded, FuelCost)
    print(Cost)
