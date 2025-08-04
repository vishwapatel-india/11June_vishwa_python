import re
data:str
data=input("Enter your username:")

x=re.findall("A-Za-z0-9",data)
if x:
    print("User registered")
else:
    print("Error")


