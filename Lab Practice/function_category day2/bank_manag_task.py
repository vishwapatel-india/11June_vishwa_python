"""Bank MAnagement system______
========================================
1) Account operation= A/c no,holder name,type
2) Deposit=min2000
3)withdrawal= moret han balance
4)satement=ac no/ac holder/ac type/balance"""

#function defining
def account(no,name,type):

    #withdrwl(condition):
    #stment(acno,acname,actype,bal):
    return no,name,type 

def account_details():
    x=account(1234,'vishwa','savings')
    print("Acc number:",x[0])
    print("Acc name:",x[1])
    print("Acc type:",x[2])

account_details()

def deposit(min):
    return min

def dep():
    y=deposit(5000)
    if y<2000:
        print('Error!! amt should be more than 2000')
    else:
        print('Total amt:')

dep()


