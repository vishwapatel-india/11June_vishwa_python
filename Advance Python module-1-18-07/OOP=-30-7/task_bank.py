import random
class account:
    acnm:str
    actype:str
    def acc(self):
        self.balance = 0
        self.acno = random.randint(111111, 999999)
        print("Account Number:", self.acno)
        self.acnm = input("Enter your account name: ")
        print("Account Holder's Name:", self.acnm)
        self.actype = input("Enter Account Type: ")
        print("Account Type:", self.actype)
        

    def deposit(self):
        depamt = int(input("Enter the amount to be deposited: "))
        if depamt < 2000:
            print("Error! Minimum deposit amount is 2000.")
        else:
            self.balance += depamt
            print("Deposit successful. Main Balance:", self.balance)

    def withdraw(self):
        withamt = int(input("Enter the amount to be withdrawn: "))
        if withamt > self.balance:
            print("Error! Amount is more than total balance.")
        else:
            self.balance -= withamt
            print("Withdrawal successful. New Balance:", self.balance)

    def statement(self):
        print("\n====== Account Details ======")
        print("Account Number:", self.acno)
        print("Account Holder's Name:", self.acnm)
        print("Account Type:", self.actype)
        print("Current Balance:", self.balance)

acc=account()
acc.deposit()
acc.withdraw()
acc.statement()