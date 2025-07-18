
import random 
import datetime

fl=open('multiple.txt','a')

n=int(input("Enter the number of students:"))
print("List of students are as follows:")
print("-----------------------------------------------")

def getdata():
    Inserted_at=datetime.datetime.now()
    ID=random.randint(111,999)
    name=input("Enter your name:")
    city=input("Enter your city:")
    fl.write(f"\nInserted_at:{Inserted_at}\nID:{ID}\nNAME:{name}\nCITY:{city}\n")
    fl.write(f"-----------------------\n")

for i in range(n):
    getdata()