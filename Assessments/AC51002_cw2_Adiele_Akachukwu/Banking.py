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
    def __init__(self, accountId, customerId, accountType, currency, accountBalance, accountStatus, CreationDate):
        self.accountId = accountId
        self.customerId = customerId
        self.accountType = accountType
        self.currency = currency
        self.accountBalance = accountBalance
        self.accountStatus = accountStatus
        self.CreationDate = CreationDate

    def __str__(self):
        pass
    
    def deposit(self):
        pass

    def withdraw(self):
        pass

# ---------------------------------------------------------------------------------------

class savingsAccount(account):
    def __init__(self, accountId, customerId, accountType, currency, accountBalance, accountStatus, CreationDate, takeInterest):
        super().__init__(accountId, customerId, accountType, currency, accountBalance, accountStatus, CreationDate)
        
        self.takeInterest = takeInterest.upper()
        if (self.takeInterest == "Y"):
            self.interestRate = 4
        

# ---------------------------------------------------------------------------------------

class currentAccount(account):
    def __init__(self, accountId, customerId, accountType, currency, accountBalance, accountStatus, CreationDate, takeInterest, overdraftAmount):
        super().__init__(accountId, customerId, accountType, currency, accountBalance, accountStatus, CreationDate)
        
        self.takeInterest = takeInterest.upper()
        if (self.takeInterest == "Y"):
            self.interestRate = 4
        
        self.overdraftAmount = overdraftAmount

    
# ---------------------------------------------------------------------------------------

class mortgageAccount(account):
    def __init__(self, accountId, customerId, accountType, currency, accountBalance, accountStatus, CreationDate, mortgageInterestRate, mortgagePrincipal, mortgageTerm, repaymentAccount):
        super().__init__(accountId, customerId, accountType, currency, accountBalance, accountStatus, CreationDate)
        
        self.mortgageInterestRate = mortgageInterestRate
        self.mortgagePrincipal = mortgagePrincipal
        self.mortgageTerm = mortgageTerm
        self.repaymentAccount = repaymentAccount
    
# ---------------------------------------------------------------------------------------

