fl=open('data.txt','w')

id= input("Enter an ID:")
name=input("Enter your name:")
city=input("Enter a city:")

fl.write(f'ID:{id}')
fl.write(f'NAME:{name}\n')
fl.write(f'CITY:{city}\n')