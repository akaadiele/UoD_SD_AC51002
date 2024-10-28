import os

# # a_string = "hello";
# print(type(a_string));
# a_string = 42;
# print(type(a_string));


# f = open("C:/Users/Akaad/OneDrive/Documents/VS_Code_Workspaces/UoD_SD_AC51002/Week_6/myfile.txt", "w")

# f = open("/DundeeZest_Files/myfile.txt", "w")

# fileName = "Assessment_1/DundeeZest_Files/myfile2.txt"
# fileName = "Assessment_1/DundeeZest_Files/aka/ProductionLogs.txt"
# staffProductionLogs = open(fileName,'w',encoding='UTF-8')



# THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
# my_file = os.path.join(THIS_FOLDER, 'copy.txt')

# print(THIS_FOLDER)
# print(my_file)


# parentFolder = os.path.dirname(os.path.abspath(__file__))
# directoryPath = parentFolder +'/DundeeZest_Files/qwerty/'
# fileName = directoryPath + 'ProductionLogs.txt'
# try:
#     os.makedirs(directoryPath)
# except FileExistsError:
#     # directory already exists
#     pass

# print("")
# print(parentFolder)
# print(directoryPath)
# print(fileName)

directoryPath = os.path.dirname(os.path.abspath(__file__)) +"/DundeeZest_Files/"
staffId = 'aka'

# with open(directoryPath + str(staffId) + "/ProductionLogs.txt", "r",encoding="UTF-8") as openedFile:
#     fileContent = openedFile.read()
#     print("Here are your production data from previous working day")
#     # for line in fileContent:
#     #     lineContent = line.strip()
#     #     print(lineContent)
#     print(fileContent)


productsCataloguePerHour = { 'bags':30, 'shirts':50, 'trousers':50, 'shoes':20, 'jackets':70}
print(len(productsCataloguePerHour))

print('')
with open(directoryPath + str(staffId) + "/Production_Logs.txt", "r",encoding="UTF-8") as openedFile:
    # fileContent = openedFile.read()
    # print(fileContent)
    for line in openedFile:
        # print(line.rstrip())
        currentContent = line.rstrip()
        currentItem , currentItemQty = currentContent.split(" - ")
        print(currentItem +" is "+ currentItemQty)
    
for i in range(0, len(productsCataloguePerHour)):
        

print('')
print('looping now')
print('')



# fileContent

# Bags - 240
# Shirts - 400
# Trousers - 400
# Shoes - 160
# Jackets - 560

# Staff Operating Hours: 8 hours 
# Total Items Produced: 1760 items
# len(productsCataloguePerHour)
    
retrievedProductionData = { "Bags":30, "Shirts":50, "Trousers":50, "Shoes":20, "Jackets":70}
    