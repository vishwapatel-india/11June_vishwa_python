data={}

n=int(input('Enter how many values you want'))

for i in range(n):
    key=input("enter the id:")
    value=input("enter the name")

    data["id"]=key
    data["name"]=value

print(data)