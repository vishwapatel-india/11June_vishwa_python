fl=open('multiple.txt','a')
n=int(input("Enter the number of students:"))
print("List of students are as follows:")
print("-----------------------------------------------")

def getdata():
    id=input("Enter an ID:")
    name=input("Enter your name:")
    city=input("Enter your city:")
    i+1



fl.write(f'ID:{id}\n')
fl.write(f"NAME:{name}\n")
fl.write(f"CITY:{city}\n")
fl.write(f"-----------------------\n")

for i in range(n):
    getdata()