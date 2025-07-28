class studinfo:
    """stid=0
    stnm="" initialization is done
"""
    stid:int
    stnm:str #declaration 

    def getdata(self):
        self.stid=input("Enter the ID:")
        self.stnm=input("Enter the name:")

class result(studinfo):
    def printdata(self):
        print("ID:",self.stid)
        print("Name:",self.stnm)

rs=result()
rs.getdata()
rs.printdata()