import random

class account:
    balance:int
    acno = random.randint(111111, 999999)
    acnm:str
    actype:str
    def account(self):
        #self.balance = 0
        self.acnm = input("Enter your account name: ")
        self.actype = input("Enter Account Type (e.g., Savings/Current): ")
        print("\nTask Done")

class deposit(account):
    def depo(self):
        self.balance= int(input("\nEnter the amount to be deposited: "))
        if self.balance < 2000:
            print("Error! Minimum deposit amount needed.")
        else:
            print("Current Balance:", self.balance)

class withdraw(deposit):
    y:float
    def withdr(self):
        withamt = float(input("\nEnter the amount to withdraw: "))
        if withamt <= self.balance:
            self.y=self.balance-withamt
            print("withdrawed!!!",self.y)

        else:
            print("Error!!!")

class statements(withdraw):   
    def show_statement(self):
        print("\n====== Account Statement ======")
        print("Account Number   :", self.acno)
        print("Account Holder   :", self.acnm)
        print("Account Type     :", self.actype)
        print("Current Balance  :",self.y)


acc = statements()
acc.account()
acc.depo()
acc.withdr()
acc.show_statement()
