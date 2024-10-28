import lab01


audiQ6 = lab01.CarData("Audi", "Q6 e-tron", 2024, "AQ12345ET67890", "E", 288.0, 131.0, 329.0, 2000 \
        , [5 , 18.6 , 54.0], 300, 20000.00)

print('Phase 1')
print(audiQ6)
audiQ6.drive(300)
print('')

print('Phase 2')
print(audiQ6)
audiQ6.drive(500)
print('')

print('Phase 3')
print(audiQ6)
audiQ6.drive(500)
print('')
