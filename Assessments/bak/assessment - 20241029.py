"""
* Course Code  : AC51002 - Software Development
* Assessment   : Course Work 1
* Developed By : Adiele Akachukwu
* Date Created : Tuesday, October 28, 2024
"""

# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------

# Importing Libraries
import sys, time, os

# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------

# 8. It should display a 'Service Required' message when the maximum limit of operating hours is
# reached (a value can be assumed for this). It should also display the total number of items
# produced since the last maintenance
# ---DONE---#
def outOfService():
    print("\n\n")
    print("Service Required")
    

    # Walk through directory, building a list with the file names within the directory
    fileNames = next(os.walk(baseDirectoryPath + "/Staff_Production_Logs/"), (None, None, []))[2]  # [] if no file
    for fileName in fileNames:
        with open( baseDirectoryPath + "/Staff_Production_Logs/"  + fileName, "r", encoding="UTF-8" ) as openedFile:
            # 10. Assume that the conveyor belt will be used by 4 operators and only one of them operates it per day. 
            # Your software should keep track of the number of items produced by each operator and
            # display their individual totals at the point of maintenance along with the other data in requirement 8 above
            #---DONE---#
            fileContent = openedFile.read()
            print("------------------------------------------\n")
            print("Production data for " + str( fileName.split('.txt')[0] ) + ": \n")
            print(fileContent + "\n") 

        # 9. It should reset all production and operational data, including total items produced and
        # operating hours, to prepare for the next production cycle. It is assumed that the routine
        # maintenance has been completed at this point.
        #---DONE---#
        with open( fileName, "w", encoding="UTF-8" ) as openedFile:
            openedFile.write('')
        
    updateOperatingHours(0, 0)
    
    # 11. Update requirement 8 above so that the information is displayed for exactly 10 seconds before
    # the system shuts down for maintenance.
    time.sleep(10)
    sys.exit()


# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------


# 7. It should be able to record the total number of items produced, in the appropriate file and
# update the value at the end of each day.
# ---DONE---#
def retrieveStaffData(operatorId, printStaffData='N'):
    
    
    try:
        with open( baseDirectoryPath + "/Staff_Production_Logs/"  + str(operatorId) +".txt", "r", encoding="UTF-8" ) as openedFile:
            fileContent = openedFile.read()
            if (printStaffData == 'Y'):
                print("\n------------------------------------------")
                print("Retrieving previous production data...")
                time.sleep(1)
                
                print("\nHere is your previous production data: \n")
                print(fileContent)
                print("------------------------------------------\n \n")
                time.sleep(2)

            with open( baseDirectoryPath + "/Staff_Production_Logs/"  + str(operatorId) +".txt", "r", encoding="UTF-8" ) as openedFile:
                for line in openedFile:
                    itemNames , itemsPerHour , previousHoursWorked , totalPerItem , totalAllItems = line.rstrip().split(",")
    except FileNotFoundError:
        if (printStaffData == 'Y'):
            print("\n------------------------------------------")
            print("***No production data history to display***")
            print("------------------------------------------\n \n")
            time.sleep(1)
            
        previousHoursWorked = 0

    return int(previousHoursWorked)

# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------
# 6. The software should be able to store the total number of items produced either in the .txt file in
# requirement 3 above or a separate file and retrieve the value at the start of the next day’s operation.
# ---DONE---#
def storeStaffData(operatorId, operatingHours, previousHoursWorked):

    if (previousHoursWorked != ""):
        operatingHours += previousHoursWorked
    
    itemNames = list(itemsCatalog.keys())
    itemsPerHour = list(itemsCatalog.values())
    totalItems = 0
    fileContent = "Items,Items per hour,Hours worked,Total (per item),Total (all items)"
        
    for i in range(0, len(itemsCatalog)):
        totalItems += itemsPerHour[i] * operatingHours
        fileContent += ( "\n" + str(itemNames[i]) + "," + str(int(itemsPerHour[i])) + "," + str(int(operatingHours)) + "," + str(int(itemsPerHour[i] * operatingHours)) + "," + str(int(totalItems))
        )

    # Write to file
    fileName = baseDirectoryPath + "/Staff_Production_Logs/"  + str(operatorId) +".txt"
    try:
        os.makedirs(baseDirectoryPath + "/Staff_Production_Logs/")
    except FileExistsError:
        # directory already exists
        pass

    with open( fileName, "w", encoding="UTF-8" ) as openedFile:
        openedFile.write(fileContent)

# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------


# 3. It should be able to store the total operating hours in a .txt file
# and retrieve the value at the start of the next day’s operation
# ---DONE---#
def retrieveOperatingHours():
    try:
        with open(
            baseDirectoryPath + "/Operating_Hours_Log.txt", "r", encoding="UTF-8"
        ) as openedFile:
            fileContent = openedFile.read()

            operatingHours = int(fileContent)
    except FileNotFoundError:
        operatingHours = 0

    return operatingHours


# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------


# 4. At the end of each day, it should update the total operating hours
# and store the updated value in the .txt file in requirement 3 above
# ---DONE---#
def updateOperatingHours(operatingHours, hoursWorked):

    operatingHours += hoursWorked

    with open( baseDirectoryPath + "/Operating_Hours_Log.txt", "w", encoding="UTF-8" ) as openedFile:
        openedFile.write(str(int(operatingHours)))
    
    return operatingHours



# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------
def logIn(clockInTime):
    operatorId = (input("\nEnter your assigned User Id: ")).upper()
    print(
        f"\nWelcome, {operatorId}. \nYour clock-in time for today is {clockInTime[0:2]}:{clockInTime[2:4]}",
        end="\n",
    )

    retrieveStaffData(operatorId, printStaffData='Y')

    hoursWorked = (int(workingHoursStop) - int(clockInTime)) / 100
    productionTime = int(clockInTime) + 100

    while productionTime <= int(workingHoursStop):
        # 2. Once operation commences, the software will continue to monitor production
        # until the daily limit of operating hours is reached i.e. 9am – 5pm.
        # Assume 1 hour to be equivalent to a single count by the Python interpreter e.g. a count from 1 to 2 makes 1 hour.
        # ---DONE---#
        print(f"[Time: {str(productionTime)[0:2]}:{str(productionTime)[2:4]} ... Production is progress]")
        
        currentOperatingHours = retrieveOperatingHours() + ( (productionTime - int(clockInTime)) / 100)
        if (currentOperatingHours >= operatingHoursLimit):
            hoursWorked = (productionTime - int(clockInTime)) / 100
            storeStaffData(operatorId, hoursWorked, retrieveStaffData(operatorId))
            updateOperatingHours(retrieveOperatingHours(), hoursWorked)
            outOfService()
        
        productionTime += 100

    print("\n...Production Concluded...")

    return operatorId, hoursWorked


# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------
# Declaring Global Variables:

currentTime = 0 ; operatingHoursLimit = 50
workingHoursStart = 900 ; workingHoursStop = 1700

# Task 5
itemsCatalog = {
    "Bags": 30,
    "Shirts": 50,
    "Trousers": 50,
    "Shoes": 20,
    "Jackets": 70,
}

# Get the root directory for the location of python program
baseDirectoryPath = os.path.dirname(os.path.abspath(__file__)) + "/DundeeZest_Files/"
try:
    os.makedirs(baseDirectoryPath)
except FileExistsError:
    # directory already exists
    pass

# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------
# Initiating function to begin operations

# Loop through 24hour cycles
while (currentTime >= 0000) and (currentTime < 2400):
    currentTimeFmt = str(currentTime).zfill(4)
    
    print(f"\nThe time is: {currentTimeFmt[0:2]} : {currentTimeFmt[2:4]}")

    # Check if the current time falls within working hours
    if (int(currentTime) >= int(workingHoursStart)) and (int(currentTime) < int(workingHoursStop)):
        # Task 1
        print("System online...")
        print("Enter the appropriate command: ")
        print("   >>> 'START' - Begin production <<<")
        print("   >>> 'EXIT' - End production<<<")
        print("   >>> Enter any other key or leave blank to skip next check-in")
        logInPrompt = input("")
        
        currentOperatingHours = retrieveOperatingHours()
            
        if logInPrompt.upper() == "START":
            operatorId, hoursWorked = logIn(currentTimeFmt)

            updateOperatingHours(currentOperatingHours, hoursWorked)
            storeStaffData(operatorId, hoursWorked, retrieveStaffData(operatorId))

            currentTime += hoursWorked * 100
        elif logInPrompt.upper() == "EXIT":
            sys.exit()
        else:
            currentTime += 100

        if (currentOperatingHours >= operatingHoursLimit):
            outOfService()
    else:
        print("The system is currently offline")
        print("----------------------------------")
        currentTime += 100

    if (currentTime > 2300): 
        currentTime = 0
    
    time.sleep(1)
# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------