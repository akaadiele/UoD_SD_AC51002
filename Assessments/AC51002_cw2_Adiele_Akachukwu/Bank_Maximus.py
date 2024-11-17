# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------

"""
* Course Code  : AC51002 - Software Development
* Title   : Assignment 2 - Program 2 Banking application
* Developed By : Adiele Akachukwu
* Date Created : --, November --, 2024
*
* Bank Name - Bank Maximus
"""

# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------

# Importing Libraries
import Banking ; # Bank Maximus 'Banking' class
import os, sys, time, datetime

# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------
# Save bank account info
def storeAccountInfo(accountObject):
    saveState = accountObject.saveAccountState(accountsDirectory)
    if (saveState):
        print("\nFile update for account info successful")
    else:
        print("\nFile update for account info failed")
        
    # fileName = accountsDirectory  + accountObject.accountId +".txt"
    
    # fileContent = accountObject.accountId + "," + accountObject.customerId + "," + accountObject.accountType \
    #     + "," + accountObject.currency + "," + accountObject.accountBalance + "," + accountObject.creationDate \
    #         + "," + accountObject.accountStatus + "," + accountObject.applyInterest + "," + accountObject.interestRate \
    #             + "," + accountObject.overdraftAmount + "," + accountObject.mortgagePrincipal + "," + accountObject.mortgageTerm \
    #                 + "," + accountObject.repaymentAccount + "," + accountObject.mortgageInterestRate
    # try:
    #     with open( fileName, "w", encoding="UTF-8" ) as openedFile:
    #         openedFile.write(fileContent)  ; # Write to update on the file
    #         print("\nAccount created successfully")
    #         return True
    # except FileNotFoundError:
    #         print("\Account creation failed")
    #         return False
    
# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------
# Load bank account info
def getAccountInfo(accountId):

    try:
        with open( accountsDirectory + accountId +".txt", "r", encoding="UTF-8" ) as openedFile:
            fileContent = openedFile.read()
            accountId, customerId, accountType, currency, accountBalance, creationDate, accountStatus, \
                applyInterest, interestRate, overdraftAmount, mortgagePrincipal, mortgageTerm, repaymentAccount, \
                    mortgageInterestRate = fileContent.rstrip().split(",")
            
        if (accountType == '1'):
            # Savings account
            accountObject = Banking.savingsAccount(accountId, customerId, accountType, currency, accountBalance, creationDate, applyInterest)
            accountObject.accountStatus = accountStatus
            accountObject.interestRate = interestRate
        elif (accountType == '2'):
            # Current account
            accountObject = Banking.currentAccount(accountId, customerId, accountType, currency, accountBalance, creationDate, applyInterest)
            accountObject.accountStatus = accountStatus
            accountObject.interestRate = interestRate
            accountObject.overdraftAmount = overdraftAmount
        elif (accountType == '3'):
            # Mortgage account
            accountObject = Banking.mortgageAccount(accountId, customerId, accountType, currency, accountBalance, creationDate, mortgagePrincipal, mortgageTerm, repaymentAccount)
            accountObject.accountStatus = accountStatus
            accountObject.mortgagePrincipal = mortgagePrincipal
            accountObject.mortgageTerm = mortgageTerm
            accountObject.repaymentAccount = repaymentAccount
            accountObject.mortgageInterestRate = mortgageInterestRate

        return accountObject
    except FileNotFoundError:
        print("Account not found")
        return False
# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------
def viewAllAccounts(customerObject):
    for account in customerObject.customerAccountsList:
        print("\n----------------------------------")
        accountId = account.split(".txt")[0]        
        accountObject = getAccountInfo(accountId)
        print(accountObject)
        print("----------------------------------")
    
            
# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------
def accountMenu(accountId):
    print("\n----------------------------------")
    print("1 - View account balance")
    print("2 - Make a deposit")
    print("3 - Make a withdrawal")
    print("4 - View account state")
    print("# - Return to customer menu \n \n")
    inputValue = input("")

    match inputValue:
        case '1':
            accountObject = getAccountInfo(accountId)
            accountBalance = accountObject.accountBalance
            
            print("\n----------------------------------")
            print(f"Your account balance is {accountBalance}")
            print("----------------------------------")
            accountMenu(accountId)
                    
        case '2':
            depositAmount = int(input("Enter amount to deposit: "))
            accountObject.deposit(depositAmount)
            storeAccountInfo(accountObject)
            
        case '3':
            withdrawalAmount = int(input("Enter amount to withdraw: "))
            accountObject.withdraw(withdrawalAmount)
            storeAccountInfo(accountObject)
            
        case '4':
            accountObject = getAccountInfo(accountId)
            print("\n----------------------------------")
            print(accountObject)
            print("----------------------------------")
    
            

        case '#':
            homeMenu()
        
        case _:
            print("Invalid Input\n")
            time.sleep(1)
            customerMenu()
    

# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------
def createAccount(customerObject):
    print("\n----------------------------------")
    print("\nTo open a new account, follow the below prompts and provide accurate details: ")
    time.sleep(1)
    
    existingAccountsList = next(os.walk(accountsDirectory), (None, None, []))[2]  # [] if no file
    accountId = '2' + str(len(existingAccountsList)).zfill(5)
    
    customerId = customerObject.customerId
    currency = countryCurrency
    accountBalance = 0
    creationDate = str(datetime.datetime.now().day) +'/'+ str(datetime.datetime.now().month) +'/'+ str(datetime.datetime.now().year)

    
    print("\nSelect account type")
    print("Enter 1 for Savings account")
    print("Enter 2 for Current account")
    print("Enter 3 for Mortgage account")
    accountType = input("Enter code for account type")
    
    if (accountType == '1'):
        # Creating savings account
        applyInterest = input("Apply Interest? (Y/N): ")
        
        accountObject = Banking.savingsAccount(accountId, customerId, accountType, currency, accountBalance, creationDate, applyInterest)
    elif (accountType == '2'):
        # Creating Current account
        applyInterest = input("Apply Interest? (Y/N): ")
        
        accountObject = Banking.currentAccount(accountId, customerId, accountType, currency, accountBalance, creationDate, applyInterest)
    elif (accountType == '3'):
        # Creating mortgage account
        if (customerObject.customerAccountsList):
            mortgagePrincipal = input("Enter mortgage principal amount: ")
            mortgageTerm = input("Enter mortage term (years): ")
            repaymentAccount = input("Enter occupation: ")
            
            accountObject = Banking.mortgageAccount(accountId, customerId, accountType, currency, accountBalance, creationDate, mortgagePrincipal, mortgageTerm, repaymentAccount)
        else:
            print("Kindly note, you must have an existing current account with us to proceed.")
            print("\nAccount creation failed")
            return False
    else:
        print("\nAccount creation failed")
        return False
    
    
    
    if (accountObject.accountStatus == "active"):
        returnVal = storeAccountInfo(accountObject)
        return returnVal
    else:
        print("\Account creation failed")
        return False

    time.sleep(1)

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
def customerMenu(customerFile):
    firstName, lastName, dateOfBirth, phone, email, occupation, customerId, customerPassword, creationDate = fileContent.rstrip().split(",")
    loggedInCustomer = Banking.customer(firstName, lastName, dateOfBirth, phone, email, occupation, customerId, customerPassword, creationDate)
    loggedInCustomer.customerFileContent = customerFile
    
    print("\n----------------------------------")
    print("1 - Select account")
    print("2 - Interest settings")
    print("3 - Open new account")
    print("4 - View state of all accounts")
    print("# - Return to Home menu \n \n")
    inputValue = input("")
    
    match inputValue:
        case '1':
            accountCount = 1
            for account in loggedInCustomer.customerAccountsList:
                accountId = account.split(".txt")[0]
                print(f"{accountCount} - {accountId}")
                accountCount += 1 
            accountSelected = int(input("\nEnter corresponding code for your account"))
            returnVal = accountMenu(loggedInCustomer.customerAccountsList[accountSelected - 1])
            
        case '2':
            pass
            
        case '3':
            returnVal = createAccount(loggedInCustomer)
            if(returnVal):
                loggedInCustomer.customerAccountsList.append()
            else:
                customerMenu()
            
        case '4':
            viewAllAccounts(loggedInCustomer)
            

        case '#':
            homeMenu()
        
        case _:
            print("Invalid Input\n")
            time.sleep(1)
            customerMenu()

# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------
# <description>
def registerCustomer():
    print("\n----------------------------------")
    print("\nTo register as a new customer, follow the below prompts and provide accurate details: ")
    time.sleep(1)
    
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
    
    loggedInCustomer.customerAccountsList = list("")
    
    if (loggedInCustomer.status == "Created"):
        fileName = customersDirectory  + customerId +".txt"
        
        fileContent = loggedInCustomer.firstName + "," + loggedInCustomer.lastName + "," + loggedInCustomer.dateOfBirth \
            + "," + loggedInCustomer.phone + "," + loggedInCustomer.email + "," + loggedInCustomer.occupation \
                + "," + loggedInCustomer.customerId + "," + loggedInCustomer.customerPassword \
                    + "," + loggedInCustomer.creationDate + "," + loggedInCustomer.customerAccountsList
        try:
            with open( fileName, "w", encoding="UTF-8" ) as openedFile:
                openedFile.write(fileContent)  ; # Write to update on the file
                print("\nCustomer registered successfully")
                print("Proceed to login")
        except FileNotFoundError:
                print("\nCustomer creation failed")
    else:
        print("\nCustomer creation failed")

    time.sleep(1)

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
                customerMenu(fileContent)
            else:
                print("Invalid password")
                return False
    except FileNotFoundError:
        print("Customer not found")
        return False

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
            returnVal = customerLogin()
            homeMenu()
            
            
        case '2':
            registerCustomer()
            homeMenu()
            
        case '3':
            adminMenu()
        
        case '#':
            sys.exit()
        
        case _:
            print("Invalid Input\n")
            time.sleep(1)
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

countryCurrency = "GBP"
returnVal = ''

homeMenu()
