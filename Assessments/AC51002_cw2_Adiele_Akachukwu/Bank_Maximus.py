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
*
* Python Application
"""

# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------

# Importing Libraries
import Banking ; # Bank Maximus 'Banking' class
import os, sys, time, datetime  ; # Python libraries

# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------
# Save bank account info
def storeAccountInfo(accountObject):
    saveState = accountObject.saveAccountState(accountsDirectory)
    if (saveState):
        print("\nAccount updated successfully")
        return accountObject
    else:
        print("\n***! Account updated failed")
        return False
        
    # fileName = accountsDirectory  + accountObject.accountId +".txt"
    
    # fileContent = accountObject.accountId + "," + accountObject.customerLoginId + "," + accountObject.accountType \
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
    #         print("\nAccount creation failed")
    #         return False
    
# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------
# Load bank account info
def getAccountInfo(accountId):
    try:
        with open( accountsDirectory + accountId +".txt", "r", encoding="UTF-8" ) as openedFile:
            fileContent = openedFile.read()
            accountId, customerLoginId, accountType, currency, accountBalance, creationDate, accountStatus, \
                applyInterest, interestRate, overdraftAmount, mortgagePrincipal, mortgageTerm, repaymentAccount, \
                    mortgageInterestRate = fileContent.rstrip().split(",")
            
        if (accountType == '1') or (accountType == "savings account"):
            # Savings account
            accountObject = Banking.savingsAccount(accountId, customerLoginId, accountType, currency, accountBalance, creationDate, applyInterest)
            accountObject.accountStatus = accountStatus
            accountObject.interestRate = interestRate
        elif (accountType == '2') or (accountType == "current account"):
            # Current account
            accountObject = Banking.currentAccount(accountId, customerLoginId, accountType, currency, accountBalance, creationDate, applyInterest)
            accountObject.accountStatus = accountStatus
            accountObject.interestRate = interestRate
            accountObject.overdraftAmount = overdraftAmount
        elif (accountType == '3') or (accountType == "mortgage account"):
            # Mortgage account
            accountObject = Banking.mortgageAccount(accountId, customerLoginId, accountType, currency, accountBalance, creationDate, mortgagePrincipal, mortgageTerm, repaymentAccount)
            accountObject.accountStatus = accountStatus
            accountObject.mortgagePrincipal = mortgagePrincipal
            accountObject.mortgageTerm = mortgageTerm
            accountObject.repaymentAccount = repaymentAccount
            accountObject.mortgageInterestRate = mortgageInterestRate

        return accountObject
    except FileNotFoundError:
        return False
# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------
# Save Customer info
def storeCustomerInfo(customerObject):
    saveState = customerObject.saveCustomerState(customersDirectory)
    if (saveState):
        print("\nCustomer updated successfully")
        return customerObject
    else:
        print("\n***! Customer updated failed")
        return False
        # ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------
# Load bank customer info
def getCustomerInfo(customerLoginId):
    try:
        with open( customersDirectory + customerLoginId +".txt", "r", encoding="UTF-8" ) as openedFile:
            fileContent = openedFile.read()
            firstName, lastName, dateOfBirth, phone, email, occupation, customerLoginId, customerPassword, creationDate, accountsList, customerId = fileContent.rstrip().split(",")
            customerObject = Banking.customer(firstName, lastName, dateOfBirth, phone, email, occupation, customerLoginId, customerPassword, creationDate)
            customerObject.customerId = customerId
            customerObject.customerAccountsList = accountsList.split('|')
            
            return customerObject
    except FileNotFoundError:
        return False
# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------
def viewAllAccountsForCustomer(customerObject):
    for account in customerObject.customerAccountsList:
        print("\n----------------------------------")
        accountId = account.split(".txt")[0]        
        accountObject = getAccountInfo(accountId)
        if (returnVal != False):
            print(accountObject)
        else:
            print(f"\n***! Account not found - {accountId}")
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
    inputValue = input(">>> ")

    match inputValue:
        case '1':
            accountObject = getAccountInfo(accountId)
            if (accountObject != False):
                accountBalance = accountObject.accountBalance
                print("\n----------------------------------")
                print(f"Your account balance is {currencySymbol}{accountBalance}")
                print("----------------------------------")
            else:
                print("\n***! Account not found")
            
            time.sleep(1)
            accountMenu(accountId)
                    
        case '2':
            print("Enter amount to deposit (or '#' to return): ")
            inputValue = input(">>> ")
            
            if (inputValue == '#'):
                pass
            else:
                try:
                    depositAmount = float(inputValue)                
                    accountObject = getAccountInfo(accountId)
                    if (accountObject.deposit(depositAmount) == True):
                        print(f"\Deposit of {currencySymbol}{depositAmount} was successful")
                        print(f"New account balance is {accountObject.accountBalance}")

                        storeAccountInfo(accountObject)
                except ValueError:
                    print("Invalid amount entered")
            
            time.sleep(1)
            accountMenu(accountId)
            
        case '3':
            print("Enter amount to withdraw (or '#' to return): ")
            inputValue = input(">>> ")
            
            if (inputValue == '#'):
                pass
            else:
                try:
                    withdrawalAmount = float(inputValue)
                    accountObject = getAccountInfo(accountId)
                    if ( accountObject.withdraw(withdrawalAmount) == True):
                        print(f"\nWithdrawal of {currencySymbol}{withdrawalAmount} was successful")
                        print(f"New account balance is {accountObject.accountBalance}")
                        
                        storeAccountInfo(accountObject)
                except ValueError:
                    print("Invalid amount entered")
            
            time.sleep(1)
            accountMenu(accountId)
            
        case '4':
            accountObject = getAccountInfo(accountId)
            if (accountObject != False):
                print("\n----------------------------------")
                print(accountObject)
                print("----------------------------------")
            else:
                print("\n***! Account not found")
            
            time.sleep(1)
            accountMenu(accountId)

        case '#':
            time.sleep(1)
        
        case _:
            print("\n***! Invalid Input\n")
            time.sleep(1)
            accountMenu(accountId)
    

# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------
def createAccount(customerObject):
    print("\n----------------------------------")
    print("\nTo open a new account, follow the below prompts and provide accurate details: ")
    time.sleep(1)
    
    accountStatus = ''
    
    existingAccountsList = next(os.walk(accountsDirectory), (None, None, []))[2]  # [] if no file
    accountId = '213' + str(len(existingAccountsList) + 1).zfill(5)
    
    customerLoginId = customerObject.customerLoginId
    currency = "GBP"
    accountBalance = 0
    creationDate = str(todayDay) +'/'+ str(todayMonth) +'/'+ str(todayYear)

    print("\nEnter code to select account type:")
    print("   1 - Savings account")
    print("   2 - Current account")
    print("   3 - Mortgage account")
    accountType = input(">>> ")
    
    if (accountType == '1'):
        # Creating savings account
        applyInterest = input("Apply Interest? (Y/N): ")
        
        accountObject = Banking.savingsAccount(accountId, customerLoginId, accountType, currency, accountBalance, creationDate, applyInterest)
        accountStatus = accountObject.accountStatus
    elif (accountType == '2'):
        # Creating Current account
        applyInterest = input("Apply Interest? (Y/N): ")
        
        accountObject = Banking.currentAccount(accountId, customerLoginId, accountType, currency, accountBalance, creationDate, applyInterest)
        accountStatus = accountObject.accountStatus
    elif (accountType == '3'):
        # Creating mortgage account
        if ( len(customerObject.customerAccountsList) != 0):
            mortgagePrincipal = input("Enter mortgage principal amount: ")
            mortgageTerm = input("Enter mortgage term (years): ")
            repaymentAccount = input("Enter occupation: ")
            
            accountObject = Banking.mortgageAccount(accountId, customerLoginId, accountType, currency, accountBalance, creationDate, mortgagePrincipal, mortgageTerm, repaymentAccount)
            accountStatus = accountObject.accountStatus
        else:
            print("\n***! Kindly note, you must have an existing current account with us to proceed.")
            print("\n***! Account creation failed")
            time.sleep(1)
            return False
    else:
        print("\n***! Account creation failed")
        return False
    
    
    
    if (accountStatus == "active"):
        returnVal = storeAccountInfo(accountObject)
        return returnVal
    else:
        print("\n***! Account creation failed")
        return False

    time.sleep(1)

# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------
# <description>
def adminMenu():
    print("\n----------------------------------")
    print("1 - View Customers")
    print("2 - View Accounts")
    print("# - Return to Home menu \n \n")
    inputValue = input(">>> ")
    
    match inputValue:
        case '1':
            customersCount = 1
            fileNames = next(os.walk(customersDirectory), (None, None, []))[2]  # [] if no file
            if (fileNames):
                for fileName in fileNames:
                    customerLoginId = fileName.split(".txt")[0]
                    print(f"{customersCount} - {customerLoginId}")
                    customersCount += 1 
                
                print("\nEnter corresponding code for your customer (or '#' to return): ")
                inputValue = input(">>> ")
                try:
                    if (inputValue == '#'):
                        pass
                    else:
                        returnVal = getCustomerInfo(fileNames[int(inputValue) - 1].split(".txt")[0])
                        if (returnVal != False):
                            print("\n----------------------------------")
                            print(returnVal)
                        else:
                            print("\n***! Customer file not found")
                except IndexError:
                    print("\n***! Invalid input")
            else:
                print("\n***! No customer file found")

            print("\n----------------------------------")
            time.sleep(1)
            adminMenu()
            
        case '2':
            accountsCount = 1
            fileNames = next(os.walk(accountsDirectory), (None, None, []))[2]  # [] if no file
            if (fileNames):
                for fileName in fileNames:
                    accountId = fileName.split(".txt")[0]
                    print(f"{accountsCount} - {accountId}")
                    accountsCount += 1 
                
                print("\nEnter corresponding code for your account (or '#' to return): ")
                inputValue = input(">>> ")
                try:
                    if (inputValue == '#'):
                        pass
                    else:
                        returnVal = getAccountInfo(fileNames[int(inputValue) - 1].split(".txt")[0])
                        if (returnVal != False):
                            print("\n----------------------------------")
                            print(returnVal)
                        else:
                            print("\n***! Account not found")
                except IndexError:
                    print("\n***! Invalid input")
            else:
                print("\n***! No account file found")

            
            print("\n----------------------------------")
            time.sleep(1)
            adminMenu()

        case '#':
            time.sleep(1)
            homeMenu()
        
        case _:
            print("\n***! Invalid Input\n")
            time.sleep(1)
            adminMenu()
            
# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------
# <description>
def adminLogin():
    print("\n----------------------------------")
    idInput = input("Enter Admin ID: ")
    passwordInput = input("Enter Admin password: ")
    
    try:
        with open( baseDirectory +"admin.txt", "r", encoding="UTF-8" ) as openedFile:
            fileContent = openedFile.read()
            adminName, adminPassword = fileContent.rstrip().split(",")
            if (idInput.lower() == adminName.lower()) and (adminPassword.lower() == passwordInput.lower()):
                adminMenu()
            else:
                print("\n***! Invalid Credentials")
                time.sleep(1)
                return False
    except FileNotFoundError:
        print("\n***! Admin profile not found")
        return False

# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------
# <description>
def customerMenu(customerFile):
    firstName, lastName, dateOfBirth, phone, email, occupation, customerLoginId, customerPassword, creationDate, accountsList, customerId = customerFile.rstrip().split(",")
    loggedInCustomer = Banking.customer(firstName, lastName, dateOfBirth, phone, email, occupation, customerLoginId, customerPassword, creationDate)

    loggedInCustomer.customerId = customerId
    
    if (accountsList == ''):
        loggedInCustomer.customerAccountsList = ''
    else:
        loggedInCustomer.customerAccountsList = accountsList.split('|')
    numberOfAccounts = len(loggedInCustomer.customerAccountsList)
    
    print("\n----------------------------------")
    print(f"Hello {loggedInCustomer.firstName.title()},")
    print("----------------------------------\n")
    print("1 - Accounts list")
    print("2 - Open a new account")
    print("3 - View state of all accounts")
    print("# - Return to Home menu \n \n")
    inputValue = input(">>> ")
    
    match inputValue:
        case '1':
            if ( numberOfAccounts != 0):
                accountCount = 1
                for account in loggedInCustomer.customerAccountsList:
                    # accountId = account.split(".txt")[0]
                    print(f"{accountCount} - {account}")
                    accountCount += 1
                print("\nEnter corresponding code for your account (or '#' to return): ")
                inputValue = input(">>> ")
                try:
                    if (inputValue == '#'):
                        pass
                    else:
                        print("\n----------------------------------")
                        returnVal = accountMenu(loggedInCustomer.customerAccountsList[int(inputValue) - 1])
                except IndexError:
                    print("\n***! Invalid input")
            else:
                print("\n***! No account file found")
            
            time.sleep(1)
            customerMenu(customerFile)
            
        case '2':
            returnVal = createAccount(loggedInCustomer)
            if(returnVal != False):
                if ( numberOfAccounts == 0):
                    loggedInCustomer.customerAccountsList = returnVal.accountId
                else:
                    loggedInCustomer.customerAccountsList = accountsList +'|'+ returnVal.accountId
                
                storeCustomerInfo(loggedInCustomer)
                with open( customersDirectory + loggedInCustomer.customerLoginId +".txt", "r", encoding="UTF-8" ) as openedFile:
                    fileContent = openedFile.read()
                    time.sleep(1)
                    customerMenu(fileContent)
            else:
                time.sleep(1)
                customerMenu(customerFile)
            
        case '3':
            if ( numberOfAccounts != 0):
                viewAllAccountsForCustomer(loggedInCustomer)
            else:
                print("\n***! No account file found")
            
            time.sleep(1)
            customerMenu(customerFile)

        case '#':
            time.sleep(1)
            homeMenu()
        
        case _:
            print("\n***! Invalid Input\n")
            time.sleep(1)
            customerMenu(customerFile)
# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------
# <description>
def customerLogin():
    print("\n----------------------------------")
    idInput = input("Enter your Customer Login ID: ")
    passwordInput = input("Enter your Customer password: ")

    try:
        with open( customersDirectory + idInput +".txt", "r", encoding="UTF-8" ) as openedFile:
            fileContent = openedFile.read()
            firstName, lastName, dateOfBirth, phone, email, occupation, customerLoginId, customerPassword, creationDate, accountsList, customerId = fileContent.rstrip().split(",")
            if (customerPassword == passwordInput):
                customerMenu(fileContent)
            else:
                print("\n***! Invalid password")
                return False
    except FileNotFoundError:
        print("\n***! Customer not found")
        return False

# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------
# Register a new customer
# DONE
def registerCustomer():
    print("\n----------------------------------")
    print("\nTo register as a new customer, follow the below prompts and provide accurate details: \n")
    time.sleep(1)
    
    registrationStatus = ''
    
    customerLoginId = input("\nEnter preferred log in ID: ")
    returnVal = getCustomerInfo(customerLoginId.lower())
    if (returnVal != False):
        print("\n***! This id already exists")
    else:
        firstName = input("\nEnter first name: ")
        lastName = input("\nEnter last name: ")
        
        dobDay = int(input("\nEnter Date of Birth - Day: "))
        if ( (dobDay < 1) or (dobDay > 31) ):
            print("\n***! Invalid day inputted")
        else:
            dobMonth = int(input("\nEnter Date of Birth - Month: "))
            if ( (dobMonth < 1) or (dobMonth > 12) ):
                print("\n***! Invalid Month inputted")
            else:
                dobYear = int(input("\nEnter Date of Birth - Day: "))
                if ( (len(str(dobYear)) < 0) or (len(str(dobYear)) > 4) or (dobYear > todayYear) ):
                    print("\n***! Invalid year inputted")
                else:
                    dateOfBirth = str(dobDay) +'/'+ str(dobMonth) +'/'+ str(dobYear)
                    
                    phone = input("\nEnter phone: ")
                    email = input("\nEnter email: ")
                    if (email.count('@') != 1):
                        print("\n***! Invalid email inputted")
                    else:
                        occupation = input("\nEnter occupation: ")
                        creationDate = str(todayDay) +'/'+ str(todayMonth) +'/'+ str(todayYear)
                        customerPassword = input("\nEnter preferred log in Password: ")
                        
                        loggedInCustomer = Banking.customer(firstName, lastName, dateOfBirth, phone, email, occupation, customerLoginId, customerPassword, creationDate)
                        loggedInCustomer.generateCustomerId(customersDirectory)
                        registrationStatus = loggedInCustomer.status
                
    if (registrationStatus == "Created"):
        fileName = customersDirectory  + loggedInCustomer.customerLoginId +".txt"
        
        fileContent = loggedInCustomer.firstName + "," + loggedInCustomer.lastName + "," + loggedInCustomer.dateOfBirth \
            + "," + loggedInCustomer.phone + "," + loggedInCustomer.email + "," + loggedInCustomer.occupation \
                + "," + loggedInCustomer.customerLoginId + "," + loggedInCustomer.customerPassword \
                    + "," + loggedInCustomer.creationDate + "," + str(loggedInCustomer.customerAccountsList) + "," + loggedInCustomer.customerId
        try:
            with open( fileName, "w", encoding="UTF-8" ) as openedFile:
                openedFile.write(fileContent)  ; # Write to update on the file
                print("\nCustomer registered successfully")
                print("Proceed to login")
        except FileNotFoundError:
                print("\n***! Customer creation failed")
    else:
        print("\n***! Customer creation failed")
    time.sleep(1)

# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------
# <description>
def homeMenu():
    print("\n----------------------------------")
    print("\nWelcome to Bank Maximus \n")
    print("1 - Login existing customer")
    print("2 - Register new customer")
    print("3 - Switch to Admin Menu")
    print("# - Exit Application \n \n")
    inputValue = input(">>> ")
    
    match inputValue:
        case '1':
            customerLogin()
            time.sleep(1)
            homeMenu()            
            
        case '2':
            registerCustomer()
            time.sleep(1)
            homeMenu()
            
        case '3':
            adminLogin()
            time.sleep(1)
            homeMenu()
        
        case '#':
            print("\n***! Exiting !***\n")
            time.sleep(3)
            sys.exit()
        
        case _:
            print("\n***! Invalid Input\n")
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

currencySymbol = "£"
returnVal = ''

todayDay = datetime.datetime.now().day
todayMonth = datetime.datetime.now().month
todayYear = datetime.datetime.now().year


homeMenu()