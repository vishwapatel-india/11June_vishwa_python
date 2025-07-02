stdata={}

#n=int(input('Enter how many values you want'))
keys=['id','name','city']

for i in keys:
    value=input(f"enter the value of {i}:")
    stdata[i]=value

print(stdata)