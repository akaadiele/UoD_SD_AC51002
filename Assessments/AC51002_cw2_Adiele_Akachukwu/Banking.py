# Maximus Bank

    
class person():
    def __init__(self, firstName, lastName, dateOfBirth, phone, email):
        self.firstName = firstName
        self.lastName = lastName
        self.dateOfBirth = dateOfBirth
        self.phone = phone
        self.email = email

    def __str__(self):
        output = "\nHello " + self.firstName +", here are your details: \n\n"
        output += "Name: " + self.firstName + self.lastName +" \n"
        output += "Date of Birth: " + self.dateOfBirth +" \n"
        output += "Phone: " + self.phone +" \n"
        output += "Email: " + self.email +" \n"
        
        return output
        # super().__init__(firstName, lastName, dateOfBirth, phone, email, occupation, *args, **kwargs)
# ---------------------------------------------------------------------------------------
class customer(person):
    def __init__(self, firstName, lastName, dateOfBirth, phone, email, occupation, customerId, customerPassword, creationDate):
        super().__init__(firstName, lastName, dateOfBirth, phone, email)

        self.occupation = occupation
        self.customerId = customerId
        self.customerPassword = customerPassword
        self.creationDate = creationDate
        self.customerId = customerId
        self.customerPassword = customerPassword
        self.creationDate = creationDate
        
        self.status = "Created"
        self.customerFileContent = ""
        self.customerAccountsList = []
    
    def __str__(self):
        output = "\nHello " + self.firstName +", here are your details: \n\n"
        output += "Name: " + self.firstName + self.lastName +" \n"
        output += "Date of Birth: " + self.dateOfBirth +" \n"
        output += "Phone: " + self.phone +" \n"
        output += "Email: " + self.email +" \n"
        output += "Occupation: " + self.occupation +" \n"
        output += "ID: " + self.customerId +" \n"
        output += "Joined: " + self.creationDate +" \n"
        
        return output
    
    def get(self):
        self.customerFileContent
        self.customerId

# ---------------------------------------------------------------------------------------
class admin(person):
    def __init__(self, firstName, lastName, dateOfBirth, phone, email, role, adminId, adminPassword):
        super().__init__(firstName, lastName, dateOfBirth, phone, email)
        
        self.role = role
        self.adminId = adminId
        self.adminPassword = adminPassword        

    def __str__(self):
        output = "\nHello " + self.firstName +", here are your details: \n\n"
        output += "Name: " + self.firstName + self.lastName +" \n"
        output += "Date of Birth: " + self.dateOfBirth +" \n"
        output += "Phone: " + self.phone +" \n"
        output += "Email: " + self.email +" \n"
        output += "ID: " + self.adminId +" \n"
        output += "Role: " + self.role +" \n"
        
        return output
# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------
class account():
    def __init__(self, accountId, customerId, accountType, currency, accountBalance, creationDate):
        self.accountId = accountId
        self.customerId = customerId
        self.accountType = accountType
        self.currency = currency
        self.accountBalance = int(accountBalance)
        self.creationDate = creationDate
        
        self.accountStatus = "active"
        


    def deposit(self, depositAmount):
        self.accountBalance += depositAmount
        print(f"\nDeposit of {self.currency}{depositAmount} was successful")
        print(f"New account balance is {self.accountBalance}")

    def withdraw(self, withdrawalAmount):
        self.accountBalance -= withdrawalAmount
        print(f"\nWithdrawal of {self.currency}{withdrawalAmount} was successful")
        print(f"New account balance is {self.accountBalance}")


    def saveAccountState(self, accountsDirectory):
        applyInterest = interestRate = overdraftAmount = mortgagePrincipal = ''
        mortgageTerm = repaymentAccount = repaymentAccount = mortgageInterestRate = ''
        
        fileName = accountsDirectory  + self.accountId +".txt"
        
        fileContent = self.accountId + "," + self.customerId + "," + self.accountType \
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
        output += "\nCustomer Id: " + self.customerId
        output += "\nAccount Type: " + self.accountType
        output += "\nAccount Balance: " + self.currency + str(self.accountBalance)
        output += "\nAccount Created On: " + self.creationDate
        
        return output
    
# ---------------------------------------------------------------------------------------

class savingsAccount(account):
    def __init__(self, accountId, customerId, accountType, currency, accountBalance, creationDate, applyInterest):
        super().__init__(accountId, customerId, accountType, currency, accountBalance, creationDate)
        
        self.applyInterest = applyInterest.upper()
        if (self.applyInterest == "Y"):
            self.interestRate = 4
        
    def saveAccountState(self, accountsDirectory):
        overdraftAmount = mortgagePrincipal = mortgageTerm = ''
        repaymentAccount = mortgageInterestRate = ''
        
        fileName = accountsDirectory  + self.accountId +".txt"
        
        fileContent = self.accountId + "," + self.customerId + "," + self.accountType \
            + "," + self.currency + "," + str(self.accountBalance) + "," + self.creationDate \
                + "," + self.accountStatus + "," + self.applyInterest + "," + self.interestRate \
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
        output += "\nCustomer Id: " + self.customerId
        output += "\nAccount Type: " + self.accountType
        output += "\nAccount Balance: " + self.currency + str(self.accountBalance)
        output += "\nApply Interest?: " + self.applyInterest
        output += "\nCurrent Month's interest: " + str(self.calculateInterestAmount())
        output += "\nAccount Created On: " + self.creationDate
        
        return output



# ---------------------------------------------------------------------------------------

class currentAccount(account):
    def __init__(self, accountId, customerId, accountType, currency, accountBalance, creationDate, applyInterest):
        super().__init__(accountId, customerId, accountType, currency, accountBalance, creationDate)
        
        self.applyInterest = applyInterest.upper()
        if (self.applyInterest == "Y"):
            self.interestRate = 4
        
        self.overdraftAmount = 100


    def saveAccountState(self, accountsDirectory):
        mortgagePrincipal = mortgageTerm = ''
        repaymentAccount = mortgageInterestRate = ''
        
        fileName = accountsDirectory  + self.accountId +".txt"
        
        fileContent = self.accountId + "," + self.customerId + "," + self.accountType \
            + "," + self.currency + "," + str(self.accountBalance) + "," + self.creationDate \
                + "," + self.accountStatus + "," + self.applyInterest + "," + self.interestRate \
                    + "," + self.overdraftAmount + "," + mortgagePrincipal + "," + mortgageTerm \
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
        output += "\nCustomer Id: " + self.customerId
        output += "\nAccount Type: " + self.accountType
        output += "\nAccount Balance: " + self.currency + str(self.accountBalance)
        output += "\nOverdraft allowed: " + self.currency + str(self.overdraftAmount)
        output += "\nApply Interest?: " + self.applyInterest
        output += "\nCurrent Month's interest: " + self.currency + str(self.calculateInterestAmount())
        output += "\nAccount Created On: " + self.creationDate
                
        return output

# ---------------------------------------------------------------------------------------

class mortgageAccount(account):
    def __init__(self, accountId, customerId, accountType, currency, accountBalance, creationDate, mortgagePrincipal, mortgageTerm, repaymentAccount):
        super().__init__(accountId, customerId, accountType, currency, accountBalance, creationDate)
        
        self.mortgagePrincipal = mortgagePrincipal
        self.mortgageTerm = int(mortgageTerm)
        self.repaymentAccount = repaymentAccount
        
        if (self.mortgageTerm <= 2):
            self.mortgageInterestRate = 5
        else:
            self.mortgageInterestRate = 6
    
    def __str__(self):
        output = "Account Id: " + self.accountId
        output += "\nCustomer Id: " + self.customerId
        output += "\nAccount Type: " + self.accountType
        output += "\nAccount Balance: " + self.currency + str(self.accountBalance)
        output += "\nAccount Created On: " + self.creationDate

        output += "\nMortgage Principal: " + self.mortgagePrincipal
        output += "\nMortgage Term : " + str(self.mortgageTerm) + "years"
        output += "\nnMortgage Repayment Account: " + self.repaymentAccount
        output += "\nnMortgage Rate: " + self.mortgageInterestRate
        
        return output

    def saveAccountState(self, accountsDirectory):
        applyInterest = interestRate = overdraftAmount = ''
        
        fileName = accountsDirectory  + self.accountId +".txt"
        
        fileContent = self.accountId + "," + self.customerId + "," + self.accountType \
            + "," + self.currency + "," + str(self.accountBalance) + "," + self.creationDate \
                + "," + self.accountStatus + "," + applyInterest + "," + interestRate \
                    + "," + overdraftAmount + "," + self.mortgagePrincipal + "," + self.mortgageTerm \
                        + "," + self.repaymentAccount + "," + self.mortgageInterestRate
        try:
            with open( fileName, "w", encoding="UTF-8" ) as openedFile:
                openedFile.write(fileContent)  ; # Write to update on the file
                return True
        except FileNotFoundError:
                return False


# ---------------------------------------------------------------------------------------

