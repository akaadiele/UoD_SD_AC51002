import sys, random, time, os


# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------


# 8. It should display a 'Service Required' message when the maximum limit of operating hours is
# reached (a value can be assumed for this). It should also display the total number of items
# produced since the last maintenance
def outOfService():
    print("Service Required")

    # 10. Assume that the conveyor belt will be used by 4 operators and only one of them operates it per
    # day. Your software should keep track of the number of items produced by each operator and
    # display their individual totals at the point of maintenance along with the other data in
    # requirement 8 above

    # 9. It should reset all production and operational data, including total items produced and
    # operating hours, to prepare for the next production cycle. It is assumed that the routine
    # maintenance has been completed at this point.
    # <statements>

    # 11. Update requirement 8 above so that the information is displayed for exactly 10 seconds before
    # the system shuts down for maintenance.
    time.sleep(10)
    sys.exit()


# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------


# 7. It should be able to record the total number of items produced, in the appropriate file and
# update the value at the end of each day.
def retrieveStaffData(staffId, printStaffData='N'):
    print("------------------------------------------ \n")
    try:
        with open(
            directoryPath + str(staffId) + "/Production_Logs.txt", "r", encoding="UTF-8"
        ) as openedFile:
            fileContent = openedFile.read()
            if (printStaffData == 'Y'):
                print("Here are your production data from previous working day: \n")
                print("Item - Quantity Produced\n")
                print(fileContent)
    except FileNotFoundError:
        print("You do not have previous production data to display.")

    print("\n ------------------------------------------\n \n")

    # fileContent
    
    # Item, units per hour, hours worked, total units (per item),         total units (all items)Bags,30,8.0,240,240.0
    # Shirts,50,8.0,400,640.0
    # Trousers,50,8.0,400,1040.0
    # Shoes,20,8.0,160,1200.0
    # Jackets,70,8.0,560,1760.0

    # Staff Operating Hours: 8 hours 
    # Total Items Produced: 1760 items

    retrievedProductionData = {
        "Bags": 30,
        "Shirts": 50,
        "Trousers": 50,
        "Shoes": 20,
        "Jackets": 70,
    }

    return retrievedProductionData


# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------
# 6. The software should be able to store the total number of items produced either in the .txt file in
# requirement 3 above or a separate file and retrieve the value at the start of the next day’s operation.
# ---DONE---#
def storeStaffData(userId, operatingHours, retrievedProductionData):

    if retrievedProductionData != "":
        staffProductionData = retrievedProductionData
    else:
        staffProductionData = productsCataloguePerHour

    itemNames = list(staffProductionData.keys())
    itemQtyPerHr = list(staffProductionData.values())
    totalItems = 0
    fileContent = "Item,Units per hour,Hours worked,Total units (per item),Total units (all items)"
        # , Days worked before maintenance"
    for i in range(0, len(staffProductionData)):
        totalItems += itemQtyPerHr[i] * operatingHours
        fileContent += ( "\n" + str(itemNames[i]) + "," + str(itemQtyPerHr[i]) + "," + str(operatingHours) + "," + str(int(itemQtyPerHr[i] * operatingHours)) + "," + str(totalItems)
        )
        # +","+ daysCount+"\n"

    # Write to file
    fileName = directoryPath + str(userId) + "/Production_Logs.txt"
    try:
        os.makedirs(directoryPath + str(userId))
    except FileExistsError:
        # directory already exists
        pass

    # fileContent += (
    # Item,Units per hour,Hours worked,Total units (per item),Total units (all items)
    # Bags,30,8.0,240,240.0
    # Shirts,50,8.0,400,640.0
    # Trousers,50,8.0,400,1040.0
    # Shoes,20,8.0,160,1200.0
    # Jackets,70,8.0,560,1760.0

    staffProductionLogs = open(fileName, "w", encoding="UTF-8")
    staffProductionLogs.write(fileContent)
    staffProductionLogs.close()


# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------


# 3. It should be able to store the total operating hours in a .txt file
# and retrieve the value at the start of the next day’s operation
# ---DONE---#
def retrieveOperatingHours():
    try:
        with open(
            directoryPath + "/Operating_Hours_Log.txt", "r", encoding="UTF-8"
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

    with open(
        directoryPath + "/Operating_Hours_Log.txt", "w", encoding="UTF-8"
    ) as openedFile:
        openedFile.write(str(int(operatingHours)))


# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------


def logIn(clockInTime):
    logInId = input("\nEnter your assigned User Id: ")
    print(
        f"\nWelcome, {logInId}. \nYour clock-in time for today is {clockInTime[0:2]}:{clockInTime[2:4]}",
        end="\n",
    )

    print("\nRetrieving previous production data...")
    retrieveStaffData(logInId, printStaffData='Y')

    hoursWorked = (int(workingHoursStop) - int(clockInTime)) / 100
    productionTime = int(clockInTime) + 100

    while productionTime <= int(workingHoursStop):
        # 2. Once operation commences, the software will continue to monitor production
        # until the daily limit of operating hours is reached i.e. 9am – 5pm.
        # Assume 1 hour to be equivalent to a single count by the Python interpreter e.g. a count from 1 to 2 makes 1 hour.
        # ---DONE---#
        print(
            f"Production is progress... [Time: {str(productionTime)[0:2]}:{str(productionTime)[2:4]}]"
        )
        productionTime += 100

    #   {str(productionTime).zfill(4)}]")

    print("\n...Production Concluded...")

    return logInId, hoursWorked


# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------


def commenceOperation(currentTime):
    while (currentTime >= 0000) and (currentTime < 2400):
        currentTimeFmt = str(currentTime).zfill(4)
        currentTimeHr = currentTimeFmt[0:2]
        currentTimeMin = currentTimeFmt[2:4]

        print(f"\nThe time is: {currentTimeHr} : {currentTimeMin}")

        if (int(currentTime) >= int(workingHoursStart)) and (
            int(currentTime) < int(workingHoursStop)
        ):
            # 1. It should allow an operator to start production for each day by typing in an input. You can decide
            # what this input will be. The input cannot change and operation for the day cannot commence without it
            # ---DONE---#
            print("System online...")
            print(
                "input the appropriate command: 'START' to begin production or any other key to skip: "
            )
            print(">>> 'START' - to begin production <<<")
            print(">>> 'EXIT' - to end program <<<")
            print("or leave blank to skip")
            logInPrompt = input("")
            if logInPrompt.upper() == "START":
                logInId, hoursWorked = logIn(currentTimeFmt)

                # 3. & 4.
                updateOperatingHours(retrieveOperatingHours(), hoursWorked)

                # 6.
                storeStaffData(logInId, hoursWorked, retrieveStaffData(logInId))

                currentTime += hoursWorked * 100

            elif logInPrompt.upper() == "EXIT":
                sys.exit()
            else:
                currentTime += 100
        else:
            print("The system is currently offline")
            print("----------------------------------")
            currentTime += 100

        time.sleep(1)


# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------

# 5. Include in the software a set value for the number of items that can be produced in an hour (e.g.,
# 100 items/hour). This could be a fixed value.
# ---DONE---#
productsCataloguePerHour = {
    "Bags": 30,
    "Shirts": 50,
    "Trousers": 50,
    "Shoes": 20,
    "Jackets": 70,
}

directoryPath = os.path.dirname(os.path.abspath(__file__)) + "/DundeeZest_Files/"
try:
    os.makedirs(directoryPath)
except FileExistsError:
    # directory already exists
    pass

operatingHoursMax = 40
workingHoursStart = 900
workingHoursStop = 1700
# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------
commenceOperation(900)

# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------
