import sys, random, time, os


def retrieveStaffData(staffId):
# 10. Assume that the conveyor belt will be used by 4 operators and only one of them operates it per
# day. Your software should keep track of the number of items produced by each operator and
# display their individual totals at the point of maintenance along with the other data in
# requirement 8 above
    # <statements>
    print('')
    
# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------

# 8. It should display a 'Service Required' message when the maximum limit of operating hours is
# reached (a value can be assumed for this). It should also display the total number of items
# produced since the last maintenance
def outOfService():
    print("Service required")
    
    
# 9. It should reset all production and operational data, including total items produced and
# operating hours, to prepare for the next production cycle. It is assumed that the routine
# maintenance has been completed at this point.
    # <statements>

# 11. Update requirement 8 above so that the information is displayed for exactly 10 seconds before
# the system shuts down for maintenance.
    time.sleep(10)

    return print("Service Completed")
# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------

# 7. It should be able to record the total number of items produced, in the appropriate file and
# update the value at the end of each day.
def updateProductionStats(userId, operatingHours):
    operatingHours = operatingHours / 100
    
    
    # productsCataloguePerHour = { 'bags':30, 'shirts':50, 'trousers':50, 'shoes':20, 'jackets':70}
    fileContent = '' ; totalItems = 0
    for i in range(0, len(productsCataloguePerHour)):
        fileContent += itemNames[i] + "," + str(int(itemQtyPerHr[i]))  + "," + str(int(operatingHours)) + "," + str(int(itemQtyPerHr[i] * operatingHours)) + "\n"
        totalItems += (itemQtyPerHr[i] * operatingHours)
    
    # write to file
    headerLine = "Item Name,Unit Produced Per Hour,Hours Operated,Quantity Produced"
    footerLine = "Grand Total = "+ str(int(totalItems))
    
    directoryPath = parentFolder +'/DundeeZest_Files/'+ str(userId)
    fileName = directoryPath + '/ProductionLogs.txt'
    try:
        os.makedirs(directoryPath)
    except FileExistsError:
        # directory already exists
        pass
    
    staffProductionLogs = open(fileName,'w',encoding='UTF-8')
    staffProductionLogs.write(headerLine +'\n'+ fileContent +'\n'+ footerLine)
    staffProductionLogs.close()
    
    # with open(fileName, "w",encoding='UTF-8') as staffProductionLogs:
    #     staffProductionLogs.write(fileContent)

    


# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------

def logIn(clockInTime):
    logInId = input("Enter your assigned User Id: ")
    print('Welcome, ', logInId,'. Your clock in time is ', clockInTime[0:2] + ":" + clockInTime[2:4], end='\n')
    
# retrieve
# 3. It should be able to store the total operating hours in a .txt file 
# and retrieve the value at the start of the next day’s operation


# 6. The software should be able to store the total number of items produced either in the .txt file in
# requirement 3 above or a separate file and retrieve the value at the start of the next day’s operation.
        # read from file

    hoursWorked = workingHoursStop - int(clockInTime)
    productionTime = int(clockInTime)
    
    while (productionTime <= workingHoursStop):
        print(f'Production is progress... [Time: {str(productionTime).zfill(4)}]')
        productionTime += 100

    print("Production Concluded...")
    
    # store
# 3. It should be able to store the total operating hours in a .txt file 
# and retrieve the value at the start of the next day’s operation

    return logInId, hoursWorked
    
    
# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------

def clockInCheck(currentTime):
    while ((currentTime >= 0000) and (currentTime < 2400)):
        currentTimeFmt = str(currentTime).zfill(4)
        currentTimeHr = currentTimeFmt[0:2]
        currentTimeMin = currentTimeFmt[2:4]
        
        print(f"\nThe time is: {currentTimeHr} : {currentTimeMin}")
        
        if ((currentTime >= 900) and (currentTime < 1700)):
# 1. It should allow an operator to start production for each day by typing in an input. You can decide
# what this input will be. The input cannot change and operation for the day cannot commence without it
###
            print("System online...")
            print("Enter the word 'START' to begin production or any other key to skip: ")
            logInPrompt = input("")
            if (logInPrompt.upper() == 'START'):
                logInId, hoursWorked = logIn(currentTimeFmt)
                currentTime += hoursWorked
# 4. At the end of each day, it should update the total operating hours 
# and store the updated value in the .txt file in requirement 3 above

                updateProductionStats(logInId, hoursWorked)
                
            elif (logInPrompt.upper() == 'EXIT'):
                    sys.exit()
            else:
                pass
        else:
            print("The system is currently offline")
            print("----------------------------------")
            currentTime += 100
            
        time.sleep(1)


    
# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------

# 5. Include in the software a set value for the number of items that can be produced in an hour (e.g.,
# 100 items/hour). This could be a fixed value.
productsCataloguePerHour = { 'bags':30, 'shirts':50, 'trousers':50, 'shoes':20, 'jackets':70}
itemNames = list(productsCataloguePerHour.keys())
itemQtyPerHr = list(productsCataloguePerHour.values())

parentFolder = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------
operatingHoursMax = 40

workingHoursStart = 900 ; workingHoursStop = 1700

# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------
clockInCheck(800)

    
# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------

