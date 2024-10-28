# """
# 1. Write your own class
# Design a class called CarData which allows the user to store information about a car:
# Information should be held in the form of integers, decimal numbers, or char
# variables. Possible information to be stored could include dimensions, weight, top
# speed, miles per gallon, price, year of registration, whether car has antilock brakes
# (‘Y’ or ‘N’), whether the car is from the factory or used (‘F’ or ‘U’) etc. Start by
# representing the class in diagrammatic form. Include all necessary class methods
# and attributes, distinguishing between public and private members.
# Write a Python implementation for your class. Write a suitable default
# constructor/initialiser for your class. Write a second constructor which takes one or
# more arguments. all the necessary class functions. In a separate code file, write code
# to use and test this class by creating at least one object of the class CarData, and
# perform some operations on it
# """

class CarData:
    brand = ""          # Toyota, Ford
    model = ""          # Avalon, Explorer
    year = None             # 2024
    chassisNumber = ""        # QWE1234
    powerSource = ""        # P-petrol, D-diesel, E-electric, H-hybrid
    horsePower = None       # value in HP
    topSpeed = None         # value in Mph
    milesRange = None         # value in Miles
    weight = None         # value in kg
    dimensions = []         #  [Num. of Seats , Boot capacity (ft) , Boot First Row (ft) ]
    mileage = None          # value in Miles
    price = None         # value in GBP
    saleCondition = ""      # F-Factory New, U-used


    def __init__(self, brand, model, year, chassisNumber, powerSource, horsePower, topSpeed, milesRange, weight, dimensions, mileage, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.chassisNumber = chassisNumber
        self.powerSource = powerSource.upper()
        self.horsePower = horsePower
        self.topSpeed = topSpeed
        self.milesRange = milesRange
        self.weight = weight
        self.dimensions = dimensions
        self.mileage = mileage
        self.price = price
        
        if (self.mileage > 1000):
            self.saleCondition = 'F'    #Factory new
            self.saleConditionDesc = "Factory New"
        else:
            self.saleCondition = 'U'    #Used
            self.saleConditionDesc = "Used"
        
        
        if (self.powerSource == "P") :
            self.powerSourceDesc = "Petrol"
        elif (self.powerSource == "D") :
            self.powerSourceDesc = "Diesel"
        elif (self.powerSource == "E") :
            self.powerSourceDesc = "Electric"
        elif (self.powerSource == "H") :
            self.powerSourceDesc = "Hybrid"
        else:
            self.powerSourceDesc = "Invalid input!"

        
    def drive(self, distanceMile):
        print('The car has now driven an additional {}miles'.format(distanceMile) )
        
        self.mileage += distanceMile
        if (self.mileage > 1000):
            self.saleCondition = "F"    #Factory new
        else:
            self.saleCondition = "U"    #Used


    def __str__(self):
        carInfo = "Brand: {0}. \nModel: {1}. \nYear: {2}. \nChassis Number: {3}. \nPower Source: {4}. \nHorsepower: {5}hp. \n" \
                    "Top Speed: {6}mph. \nMiles Range: {7}miles. \nWeight: {8}kg. \nDimensions: {9}. \nPrice: {10}. \nMileage: {11}miles. \n" \
                    "Condition: {12}. \n".format(self.brand,self.model ,self.year ,self.chassisNumber ,self.powerSourceDesc ,self.horsePower\
                    ,self.topSpeed ,self.milesRange ,self.weight ,self.dimensions ,self.price ,self.mileage ,self.saleConditionDesc)
        
        return carInfo
        
        

class ForSale(CarData):
    def __init__(self, brand, model, year, chassisNumber, powerSource, horsePower, topSpeed, milesRange, weight, dimensions, mileage, price, advert = ''):
        super().__init__(brand, model, year, chassisNumber, powerSource, horsePower, topSpeed, milesRange, weight, dimensions, mileage, price)
        self.advert = 'This ' + str(self.year) +' '+ str(self.brand) +' '+ str(self.model) + ' is for sale at price of GBP' + str(self.price)
        
    def __str__(self):
        return self.advert


class ForRent(CarData):
    def __init__(self, brand, model, year, chassisNumber, powerSource, horsePower, topSpeed, milesRange, weight, dimensions, mileage, price, rentRange = 'daily', costPerDay = 100):
        super().__init__(brand, model, year, chassisNumber, powerSource, horsePower, topSpeed, milesRange, weight, dimensions, mileage, price)
        
        self.rentRange = rentRange     ; # Number of days rent
        self.costPerDay = costPerDay

    def __str__(self):
        outputText = 'This ' + str(self.year) +' '+ str(self.brand) +' '+ str(self.model) + ' is for rent at price of GBP' + str(self.price) +' '+ str(self.rentRange)
        return outputText


