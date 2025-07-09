def acc_details(name,ty,city,bal=0):
    print("Account holder's name:",name)
    print("type:",ty)
    print("City/Branch:",city)
    print("balance",bal)

def dep():
    a=int(input("Enter the amt to be deposited"))

def withdraw():
    b=int(input("Enter amt to be withdrawed"))
    if b<a:
        print("Balance:",a-b)
    else:
        print("amt should be less the Balance")