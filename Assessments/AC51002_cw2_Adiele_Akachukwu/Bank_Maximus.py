# Bank Maximus


import os, sys, time, datetime
import Banking


# Save bank account info

# Load bank account info

# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------
# <description>
def adminMenu():
    print("\n----------------------------------")
    idInput = input("Enter your Admin ID")
    passwordInput = input("Enter your Admin password")

# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------
# <description>
def customerMenu(loggedInCustomer):
    loggedInCustomer
    
    print("\n----------------------------------")
    print("\nWelcome to Bank Maximus \n")
    print("1 - Select account")
    print("2 - Interest settings")
    print("3 - Open new account")
    print("# - Logout \n \n")
    
    inputValue = input("")
    
    match inputValue:
        case '1':
            pass
            
        case '2':
            pass
            
        case '3':
            pass
        
        case '#':
            homeMenu()
        
        case _:
            print("Invalid Input\n")
            time.sleep(2)
            homeMenu()

# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------
# <description>
def registerCustomer():
    print("\n----------------------------------")
    print("\nTo register as a new customer, follow the below prompts and provide accurate details: ")
    time.sleep(2)
    
    firstName = input("Enter first name: ")
    lastName = input("Enter last name: ")
    
    dobDay = input("Enter Date of Birth - Day: ")
    # if ( (dobDay < 1) or (dobDay > 31) ):
    #     print("Invalid day inputted")
    # else:
    dobMonth = input("Enter Date of Birth - Month: ")
    dobYear = input("Enter Date of Birth - Day: ")
    dateOfBirth = dobDay +'/'+ dobMonth +'/'+ dobYear
    
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    occupation = input("Enter occupation: ")
    customerId = input("Enter preferred log in ID: ")
    customerPassword = input("Enter preferred log in Password: ")
    
    creationDate = str(datetime.datetime.now().day) +'/'+ str(datetime.datetime.now().month) +'/'+ str(datetime.datetime.now().year)
    
    loggedInCustomer = Banking.customer(firstName, lastName, dateOfBirth, phone, email, occupation, customerId, customerPassword, creationDate)
    
    
    if (loggedInCustomer.status == "Created"):
        fileName = customersDirectory  + customerId +".txt"
        
        fileContent = loggedInCustomer.firstName + "," + loggedInCustomer.lastName + "," + loggedInCustomer.dateOfBirth \
            + "," + loggedInCustomer.phone + "," + loggedInCustomer.email + "," + loggedInCustomer.occupation \
                + "," + loggedInCustomer.customerId + "," + loggedInCustomer.customerPassword + "," + loggedInCustomer.creationDate
        try:
            with open( fileName, "w", encoding="UTF-8" ) as openedFile:
                openedFile.write(fileContent)  ; # Write to update on the file
                print("\nCustomer registered successfully")
                print("Proceed to login")
        except FileNotFoundError:
                print("\nCustomer creation failed")
    else:
        print("\nCustomer creation failed")

    time.sleep(2)

# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------
# <description>
def customerLogin():
    print("\n----------------------------------")
    idInput = input("Enter your Customer ID")
    passwordInput = input("Enter your Customer password")
            
    try:
        with open( customersDirectory + idInput +".txt", "r", encoding="UTF-8" ) as openedFile:
            fileContent = openedFile.read()
            firstName, lastName, dateOfBirth, phone, email, occupation, customerId, customerPassword, creationDate = fileContent.rstrip().split(",")
            if (customerPassword == passwordInput):
                loggedInCustomer = Banking.customer(firstName, lastName, dateOfBirth, phone, email, occupation, customerId, customerPassword, creationDate)
                loggedInCustomer.customerFileContent = fileContent
                customerMenu(loggedInCustomer)
            else:
                print("Invalid password")
                return ''
    except FileNotFoundError:
        print("Customer not found")
        return ''

# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------
# <description>
def homeMenu():
    print("\n----------------------------------")
    print("\nWelcome to Bank Maximus \n")
    print("1 Login existing customer")
    print("2 Register new customer")
    print("3 Switch to Admin Menu \n \n")
    
    inputValue = input("")
    
    match inputValue:
        case '1':
            customerLogin()
            
        case '2':
            registerCustomer()
            homeMenu()
            
        case '3':
            adminMenu()
        
        case '#':
            sys.exit()
        
        case _:
            print("Invalid Input\n")
            time.sleep(2)
            homeMenu()
            


# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------

# Get the root directory for the location of python program
baseDirectory = os.path.dirname(os.path.abspath(__file__)) + "/Bank_Maximus/"
customersDirectory = baseDirectory + "/Customers/"
accountsDirectory = baseDirectory + "/Accounts/"

try:
    # Redundancy check to create directories if they do not exist
    os.makedirs(baseDirectory)
    os.makedirs(customersDirectory)
    os.makedirs(accountsDirectory)
except FileExistsError:
    # directory already exists
    pass

homeMenu()
