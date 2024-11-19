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
* 'Banking' Class File
"""

# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------

# Importing Libraries

import os
    
# ---------------------------------------------------------------------------------------
class customer():
    def __init__(self, firstName, lastName, dateOfBirth, phone, email, occupation, customerLoginId, customerPassword, creationDate):
        self.firstName = firstName.lower()
        self.lastName = lastName.lower()
        self.dateOfBirth = dateOfBirth
        self.phone = phone
        self.email = email
        self.occupation = occupation.lower()
        self.customerLoginId = customerLoginId.lower()
        self.customerPassword = customerPassword
        self.creationDate = creationDate
        
        self.status = "Created"
        self.customerAccountsList = ''

    def generateCustomerId(self, customersDirectory):
        existingCustomersList = next(os.walk(customersDirectory), (None, None, []))[2]  # [] if no file
        self.customerId = '1' + str(len(existingCustomersList) + 1).zfill(5)
        
    def saveCustomerState(self, customersDirectory):
        fileName = customersDirectory  + self.customerLoginId +".txt"
        
        fileContent = self.firstName + "," + self.lastName + "," + self.dateOfBirth \
            + "," + self.phone + "," + self.email + "," + self.occupation \
                + "," + self.customerLoginId + "," + self.customerPassword \
                    + "," + self.creationDate + "," + str(self.customerAccountsList) + "," + self.customerId
        try:
            with open( fileName, "w", encoding="UTF-8" ) as openedFile:
                openedFile.write(fileContent)  ; # Write to update on the file
                return True
        except FileNotFoundError:
                return False
            
    def __str__(self):
        
        if ( len(self.customerAccountsList) == 0):
            customerAccountsList = 'N/A'
        
        # output = "\nHello " + self.firstName.title() +", here are your details: \n\n"
        output = "\nName: " + self.firstName.title() +' '+ self.lastName.title() +" \n"
        output += "Date of Birth: " + self.dateOfBirth +" \n"
        output += "Phone: " + self.phone +" \n"
        output += "Email: " + self.email +" \n"
        output += "Occupation: " + self.occupation.title() +" \n"
        output += "ID: " + self.customerLoginId +" \n"
        output += "Joined: " + self.creationDate +" \n"
        output += "Accounts: " + str(customerAccountsList) +" \n"
        
        return output
    
    
# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------
class account():
    def __init__(self, accountId, customerLoginId, accountType, currency, accountBalance, creationDate):
        self.accountId = accountId
        self.customerLoginId = customerLoginId
        self.accountType = accountType
        self.currency = currency
        self.accountBalance = int(accountBalance)
        self.creationDate = creationDate
        
        self.accountStatus = "active"
        


    def deposit(self, depositAmount):
        self.accountBalance += depositAmount
        print(f"\nDeposit of {self.currency}{depositAmount} was successful")
        print(f"New account balance is {self.accountBalance}")
        return True

    def withdraw(self, withdrawalAmount):
        if (self.accountBalance >= withdrawalAmount):
            self.accountBalance -= withdrawalAmount
            return True
        else:
            return False


    def saveAccountState(self, accountsDirectory):
        applyInterest = interestRate = overdraftAmount = mortgagePrincipal = ''
        mortgageTerm = repaymentAccount = repaymentAccount = mortgageInterestRate = ''
        
        fileName = accountsDirectory  + self.accountId +".txt"
        
        fileContent = self.accountId + "," + self.customerLoginId + "," + self.accountType \
            + "," + self.currency + "," + str(self.accountBalance) + "," + self.creationDate \
                + "," + self.accountStatus + "," + applyInterest + "," + interestRate \
                    + "," + overdraftAmount + "," + mortgagePrincipal + "," + mortgageTerm \
                        + "," + repaymentAccount + "," + mortgageInterestRate
        try:
            with open( fileName, "w", encoding="UTF-8" ) as openedFile:
                openedFile.write(fileContent)  ; # Write to update on the file
                return True
        except FileNotFoundError:
                return False

    def __str__(self):
        output = "Account Id: " + self.accountId
        output += "\nCustomer Id: " + self.customerLoginId
        output += "\nAccount Type: " + self.accountType.title()
        output += "\nAccount Balance: " + self.currency + str(self.accountBalance)
        output += "\nAccount Created On: " + self.creationDate
        
        return output
    
# ---------------------------------------------------------------------------------------

class savingsAccount(account):
    def __init__(self, accountId, customerLoginId, accountType, currency, accountBalance, creationDate, applyInterest):
        super().__init__(accountId, customerLoginId, accountType, currency, accountBalance, creationDate)
        
        self.accountType = "savings account"
        self.applyInterest = applyInterest.upper()
        if (self.applyInterest == "Y"):
            self.interestRate = 4
        
    def saveAccountState(self, accountsDirectory):
        overdraftAmount = mortgagePrincipal = mortgageTerm = ''
        repaymentAccount = mortgageInterestRate = ''
        
        fileName = accountsDirectory  + self.accountId +".txt"
        
        fileContent = self.accountId + "," + self.customerLoginId + "," + self.accountType \
            + "," + self.currency + "," + str(self.accountBalance) + "," + self.creationDate \
                + "," + self.accountStatus + "," + self.applyInterest + "," + str(self.interestRate) \
                    + "," + overdraftAmount + "," + mortgagePrincipal + "," + mortgageTerm \
                        + "," + repaymentAccount + "," + mortgageInterestRate
        try:
            with open( fileName, "w", encoding="UTF-8" ) as openedFile:
                openedFile.write(fileContent)  ; # Write to update on the file
                return True
        except FileNotFoundError:
                return False

    def calculateInterestAmount(self):
        interestAmount = ( self.accountBalance * self.interestRate * (1 / 12) )
        return interestAmount
    
    def __str__(self):
        output = "Account Id: " + self.accountId
        output += "\nCustomer Id: " + self.customerLoginId
        output += "\nAccount Type: " + self.accountType.title()
        output += "\nAccount Balance: " + self.currency + str(self.accountBalance)
        output += "\nApply Interest?: " + self.applyInterest
        output += "\nCurrent Month's interest: " + str(self.calculateInterestAmount())
        output += "\nAccount Created On: " + self.creationDate
        
        return output



# ---------------------------------------------------------------------------------------

class currentAccount(account):
    def __init__(self, accountId, customerLoginId, accountType, currency, accountBalance, creationDate, applyInterest):
        super().__init__(accountId, customerLoginId, accountType, currency, accountBalance, creationDate)
        
        self.accountType = "current account"
        self.applyInterest = applyInterest.upper()
        if (self.applyInterest == "Y"):
            self.interestRate = 4
        
        self.overdraftAmount = 100


    def saveAccountState(self, accountsDirectory):
        mortgagePrincipal = mortgageTerm = ''
        repaymentAccount = mortgageInterestRate = ''
        
        fileName = accountsDirectory  + self.accountId +".txt"
        
        fileContent = self.accountId + "," + self.customerLoginId + "," + self.accountType \
            + "," + self.currency + "," + str(self.accountBalance) + "," + self.creationDate \
                + "," + self.accountStatus + "," + self.applyInterest + "," + str(self.interestRate) \
                    + "," + str(self.overdraftAmount) + "," + mortgagePrincipal + "," + mortgageTerm \
                        + "," + repaymentAccount + "," + mortgageInterestRate
        try:
            with open( fileName, "w", encoding="UTF-8" ) as openedFile:
                openedFile.write(fileContent)  ; # Write to update on the file
                return True
        except FileNotFoundError:
                return False

    def calculateInterestAmount(self):
        interestAmount = ( self.accountBalance * self.interestRate * (1 / 12) )
        return interestAmount
    
    def __str__(self):
        output = "Account Id: " + self.accountId
        output += "\nCustomer Id: " + self.customerLoginId
        output += "\nAccount Type: " + self.accountType.title()
        output += "\nAccount Balance: " + self.currency + str(self.accountBalance)
        output += "\nOverdraft allowed: " + self.currency + str(self.overdraftAmount)
        output += "\nApply Interest?: " + self.applyInterest
        output += "\nCurrent Month's interest: " + self.currency + str(self.calculateInterestAmount())
        output += "\nAccount Created On: " + self.creationDate
                
        return output

# ---------------------------------------------------------------------------------------

class mortgageAccount(account):
    def __init__(self, accountId, customerLoginId, accountType, currency, accountBalance, creationDate, mortgagePrincipal, mortgageTerm, repaymentAccount):
        super().__init__(accountId, customerLoginId, accountType, currency, accountBalance, creationDate)
        
        self.accountType = "mortgage account"
        self.mortgagePrincipal = mortgagePrincipal
        self.mortgageTerm = int(mortgageTerm)
        self.repaymentAccount = repaymentAccount
        
        if (self.mortgageTerm <= 2):
            self.mortgageInterestRate = 5
        else:
            self.mortgageInterestRate = 6
    
    def __str__(self):
        output = "Account Id: " + self.accountId
        output += "\nCustomer Id: " + self.customerLoginId
        output += "\nAccount Type: " + self.accountType.title()
        output += "\nAccount Balance: " + self.currency + str(self.accountBalance)
        output += "\nAccount Created On: " + self.creationDate

        output += "\nMortgage Principal: " + str(self.mortgagePrincipal)
        output += "\nMortgage Term : " + str(self.mortgageTerm) + "years"
        output += "\nnMortgage Repayment Account: " + self.repaymentAccount
        output += "\nnMortgage Rate: " + self.mortgageInterestRate
        
        return output

    def saveAccountState(self, accountsDirectory):
        applyInterest = interestRate = overdraftAmount = ''
        
        fileName = accountsDirectory  + self.accountId +".txt"
        
        fileContent = self.accountId + "," + self.customerLoginId + "," + self.accountType \
            + "," + self.currency + "," + str(self.accountBalance) + "," + self.creationDate \
                + "," + self.accountStatus + "," + applyInterest + "," + interestRate \
                    + "," + overdraftAmount + "," + str(self.mortgagePrincipal) + "," + str(self.mortgageTerm) \
                        + "," + self.repaymentAccount + "," + str(self.mortgageInterestRate)
        try:
            with open( fileName, "w", encoding="UTF-8" ) as openedFile:
                openedFile.write(fileContent)  ; # Write to update on the file
                return True
        except FileNotFoundError:
                return False


# ---------------------------------------------------------------------------------------

