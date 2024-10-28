# A python program to convert degrees from Fahrenheit to Centigrade


centValue = float(input('Input the degree value in Centigrade: '))
fahValue = ( (9 * centValue) / 5) + 32
print('The equivalent in Fahrenheit is :', fahValue)


print('Press enter to continue to reverse conversion')
input()

fahValue = float(input('Input the degree value in Fahrenheit: '))
centValue = (fahValue - 32) * (5 / 9)
print('The equivalent in Centigrade is :', centValue)