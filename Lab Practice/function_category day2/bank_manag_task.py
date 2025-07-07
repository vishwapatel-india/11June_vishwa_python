"""Bank MAnagement system______
=======================================================
1) Account operation= A/c no,holder name,type
2) Deposit=min2000
3)withdrawal= moret han balance
4)satement=ac no/ac holder/ac type/balance
========================================================
"""
acno=int(input("Enter account number:"))
acname=input("Enter account holder's name:")
actype=input("Enter account type:")
Balance=0.0000

#function defining-task-1
def account(acno,acname,actype):
    return acno,acname,actype

def acc():
    x=account(acno,acname,actype)
    print("Your account number:",x[0])
    print("Your account name:",x[1])
    print("Your account type:",x[2])

acc()

#function defining task-2
def deposit():
    global Balance
    Balance=float(input("Enter your amt you want to deposit:"))
    if Balance>=2000:
        print("Your current balnce:",Balance)
    else:
        print("Min amt needs to be 2000")
        exit()

def withdraw():
    global Balance
    with1=float(input("Enter the amt you want to withdraw:"))
    newbal = Balance-with1
    if with1 <= Balance:
        print("The amount needs to be greater than current balance amount")
    else:
        print(newbal)
        exit()

def statement():
    acc()
    deposit()
    withdraw()

statement()