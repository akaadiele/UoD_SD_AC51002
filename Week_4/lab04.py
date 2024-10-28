# Lab class

# Functions

#----------------------------------
# # TASK 15
print('TASK 15')

def balanceCheck(acctBal):
    balanceThreshold = 100
    if (acctBal < balanceThreshold):
        checkVal = False
    else:
        checkVal = True

    return checkVal


def txnPreCheck(accountHolderNumber, *accountDetails, **address):
    print('Account balance is: ', accountDetails[0])
    if (balanceCheck(accountDetails[0])):
        print("Hello, ",accountDetails[1],"You're good to go")
    else:
        print("Hello, ",accountDetails[1],"... Error- Insufficient Balance")

#acctNo = 12345 ; myAcctBal = 100

acctNo = int(input('Enter your account number: '))
myAcctBal = float(input('Enter your account balance: '))
myAcctName = input('Enter your account name: ')
txnPreCheck(acctNo, myAcctBal, myAcctName)
#
print('*****')
#----------------------------------

