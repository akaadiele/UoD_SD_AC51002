# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------

"""
* Course Code  : AC51002 - Software Development
* Title   : Assignment 1
* Developed By : Adiele Akachukwu
* Date Created : Tuesday, November 4, 2024
"""

# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------

# Importing Libraries
import os, sys, time

# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------

# Declaring Global Variables:
currentTime = 0 ; operatingHoursLimit = 50 ; workingHoursStart = 900 ; workingHoursStop = 1700

# #5
itemsCatalog = { "Bags": 30, "Shirts": 50, "Trousers": 50, "Shoes": 20, "Jackets": 70, }

# Get the root directory for the location of python program
baseDirectory = os.path.dirname(os.path.abspath(__file__)) + "/DundeeZest_Files/"
productionDataDirectory = baseDirectory + "/Production_Data/"
try:
    # Redundancy check to create directories if they do not exist
    os.makedirs(baseDirectory)
    os.makedirs(productionDataDirectory)
except FileExistsError:
    # directory already exists
    pass

# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------
# Defining Functions to be used during execution


# Resetting data stored on files
def resetData():
    # #9
    # Walk through directory, building a list with the file names within the directory
    fileNames = next(os.walk(productionDataDirectory), (None, None, []))[2]  # [] if no file
    for fileName in fileNames:
        with open( productionDataDirectory  + fileName, "w", encoding="UTF-8" ) as openedFile:
            openedFile.write("")  ;  # Reset Production Data for each operator
        
    updateOperatingHours(0,0)  ;  # Reset Operating Hours

# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------

# Initiating service maintenance
def triggerServiceMaintenance():
    # #8
    print("\n\nService Required")
    
    # Walk through directory, building a list with the file names within the directory
    fileNames = next(os.walk(productionDataDirectory), (None, None, []))[2]  # [] if no file
    for fileName in fileNames:
        with open( productionDataDirectory  + fileName, "r", encoding="UTF-8" ) as openedFile:
            # #10
            print("------------------------------------------\n")
            print("Production data for Operator - " + str( fileName.split(".txt")[0] ) + "\n")
            
            for line in openedFile:
                itemNames , itemsPerHour , previousHoursWorked , previousTotalPerItem , previousTotalAllItems = line.rstrip().split(",")
                print(itemNames +": "+ previousTotalPerItem)
            
            print("\nTotal Items: " + previousTotalAllItems)

    # #9
    resetData()

    # #11
    time.sleep(10)
    
    print("------------------------------------------\n")
    print("\n***System shutting down for maintenance***\n")
    sys.exit()

# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------

# Reading Operator Data stored on file
def retrieveOperatorData(operatorId):
    # #7
    try:
        with open( productionDataDirectory  + str(operatorId) +".txt", "r", encoding="UTF-8" ) as openedFile:
            for line in openedFile:
                itemNames , itemsPerHour , previousHoursWorked , previousTotalPerItem , previousTotalAllItems = line.rstrip().split(",")
    except FileNotFoundError:
        previousHoursWorked = 0

    return int(previousHoursWorked)

# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------

# Updating Operator Data on file
def updateOperatorData(operatorId, operatingHours, previousHoursWorked):
    # #6
    if (previousHoursWorked != ""):
        operatingHours += previousHoursWorked
    
    itemNames = list(itemsCatalog.keys())
    itemsPerHour = list(itemsCatalog.values())
    totalItems = 0
    fileContent = "Items,Quantity Produced per Hour,Hours Worked,Total (per item),Total (all items)"    ; # Including a header line for the file

    for i in range(0, len(itemsCatalog)):
        totalItems += itemsPerHour[i] * operatingHours
        fileContent += ( "\n" + str(itemNames[i]) + "," + str(int(itemsPerHour[i])) + "," + str(int(operatingHours)) + "," + str(int(itemsPerHour[i] * operatingHours)) + "," + str(int(totalItems)) )

    # Write to file
    fileName = productionDataDirectory  + str(operatorId) +".txt"
    with open( fileName, "w", encoding="UTF-8" ) as openedFile:
        openedFile.write(fileContent)

# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------

# Reading Operating Hours stored on file
def retrieveOperatingHours():
    # #3
    try:
        with open(baseDirectory + "/Operating_Hours_Log.txt", "r", encoding="UTF-8") as openedFile:
            fileContent = openedFile.read()
            operatingHours = int(fileContent)
    except FileNotFoundError:
        operatingHours = 0

    return operatingHours

# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------

# Updating Operating Hours on file
def updateOperatingHours(operatingHours, hoursWorked):
    # #4
    operatingHours += hoursWorked

    with open( baseDirectory + "/Operating_Hours_Log.txt", "w", encoding="UTF-8" ) as openedFile:
        openedFile.write(str(int(operatingHours)))
    
    return operatingHours

# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------

# Operator login and Initiate production process 
def logIn(clockInTime):
    operatorId = (input("\nEnter your assigned User Id: ")).upper()
    print(f"\nWelcome, {operatorId}." )
    print(f"\nYour clock-in time for today is {clockInTime[0:2]}:{clockInTime[2:4]}",end="\n",)

    retrieveOperatorData(operatorId)

    hoursWorked = (int(workingHoursStop) - int(clockInTime)) / 100
    currentProductionTime = int(clockInTime) + 100

    # Loop through operating hours
    while currentProductionTime < int(workingHoursStop):
        # #2
        print(f"[Time: {str(currentProductionTime)[0:2]}:{str(currentProductionTime)[2:4]}] ... Production is progress")
        
        currentOperatingHours = retrieveOperatingHours() + ( (currentProductionTime - int(clockInTime)) / 100)
        if (currentOperatingHours >= operatingHoursLimit):
            hoursWorked = (currentProductionTime - int(clockInTime)) / 100
            updateOperatorData(operatorId, hoursWorked, retrieveOperatorData(operatorId))
            updateOperatingHours(retrieveOperatingHours(), hoursWorked)
            print("!!!\n") ; time.sleep(1)
            triggerServiceMaintenance()
        
        currentProductionTime += 100
    # Loop ends

    print(f"\n   ... Production Concluded ...")

    return operatorId, hoursWorked

# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------

# Begin operations
while (currentTime >= 0000) and (currentTime < 2400):
# Loop through 24hour cycles
    currentTimeFmt = str(currentTime).zfill(4)
    
    print(f"\n[Time: {currentTimeFmt[0:2]} : {currentTimeFmt[2:4]}]")

    # Check if the current time falls within working hours
    if (int(currentTime) >= int(workingHoursStart)) and (int(currentTime) < int(workingHoursStop)):
        # #1
        print("System online ... \n----------------------------------")
        print("Enter the appropriate command and press the 'ENTER' key: ")
        print("   *** 'START' - Begin production ***")
        print("   *** 'EXIT' - End production ***")
        print("   *** Any other input or leave blank - Skip to next check-in hour ***")
        operatorInput = input(">>> ")
        
        currentOperatingHours = retrieveOperatingHours()
            
        if operatorInput.upper() == "START":
            operatorId, hoursWorked = logIn(currentTimeFmt)

            updateOperatingHours(currentOperatingHours, hoursWorked)
            updateOperatorData(operatorId, hoursWorked, retrieveOperatorData(operatorId))

            currentTime += hoursWorked * 100
        elif operatorInput.upper() == "EXIT":
            sys.exit()
        else:
            currentTime += 100

        if (currentOperatingHours >= operatingHoursLimit):
            print("!!!\n") ; time.sleep(1)
            triggerServiceMaintenance()
    else:
        print("The system is currently offline \n----------------------------------")
        currentTime += 100

    if (currentTime > 2300): 
        currentTime = 0
    
    time.sleep(1)
# Loop ends

# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------