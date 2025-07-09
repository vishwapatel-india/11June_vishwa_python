BAL=0
def acc_details():
    a=input("Enter your name:")
    print("ACC_HOLDERS NAME:",a)
    b=input("Enter account type:")
    print("Acc type:",b)
    c=input("Enter City/Branch:")
    print("Acc branch:",c)

def dep():
    global BAL
    BAL=float(input("Enter your amt you want to deposit:"))
    if BAL>=2000:
        print("Your current balnce:",BAL)
    else:
        print("Min amt needs to be 2000")
        exit()

    

def withdraw():
    with1=float(input("Enter the amt you want to withdraw:"))
    newbal = BAL-with1
    if with1 >= BAL:
        print(newbal)
    else:
        print("The amount needs to be greater than current balance amount")
        exit()

    
    
    
    