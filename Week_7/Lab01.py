import CarData

Avalon25 = CarData.ForSale("Toyota", "Avalon XLE", 2025, "TA12345GH67890", "H", 250.0, 120, 300.0, 1000 , [5 , 25.1 , 50.0], 100, 25000.00)

audiQ6 = CarData.ForRent("Audi", "Q6 e-tron", 2024, "AQ12345ET67890", "E", 288.0, 131.0, 329.0, 2000 , [5 , 18.6 , 54.0], 300, 20000.00, costPerDay=500, rentRange='Monthly')

print(Avalon25)
print ('')
print(audiQ6)



import math
print(math.sqrt(81))

result = pow(5,3)
print(result)


print(max(16,2,5))