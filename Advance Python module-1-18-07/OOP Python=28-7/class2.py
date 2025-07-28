"""print("=====Dynamic student entry=====")
n=int(input("How many students do you have"))
"""
class info:
    stid:int
    stnm:str

    def getdata(self):
        self.stid=input("Enter the ID:")
        self.stnm=input("Enter the name:")

    def printdata(self):
        print("ID:",self.stid)
        print("NAme:",self.stnm)

st=info()
st.getdata()
st.printdata()


