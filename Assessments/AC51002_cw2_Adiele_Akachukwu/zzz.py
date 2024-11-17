import datetime, Banking, os

# x = datetime.datetime.now()
# print(x)
# print(x.year)
# print(x.month)
# print(x.day)
# print(x.)


# print(datetime.datetime.now().year)
# print(datetime.datetime.now().month)
# print(datetime.datetime.now().day)




# firstName = "John"
# lastName = "Doe"
# dateOfBirth = "01/04/1990"
# phone = "1234"
# email = "jd@mail.com"
# occupation = "Doctor"
# customerId = "jd"
# customerPassword = "123"

# creationDate = str(datetime.datetime.now().day) +'/'+ str(datetime.datetime.now().month) +'/'+ str(datetime.datetime.now().year)

# loggedInCustomer = Banking.customer(firstName, lastName, dateOfBirth, phone, email, occupation, customerId, customerPassword, creationDate)

# print(loggedInCustomer.status)

# if (loggedInCustomer.status == "Created"):
#         print("Customer registered successfully")


baseDirectory = os.path.dirname(os.path.abspath(__file__)) + "/Bank_Maximus/"
customersDirectory = baseDirectory + "/Customers/"
accountsDirectory = baseDirectory + "/Accounts/"

fileNames = next(os.walk(accountsDirectory), (None, None, []))[2]  # [] if no file
print(fileNames)
print(len(fileNames))

for i in fileNames:
    print(i)