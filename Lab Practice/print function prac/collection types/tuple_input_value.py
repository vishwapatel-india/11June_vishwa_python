value=[]

n=int(input('Enter total number of city'))

for i in range(n):
    city=input('Enter name of city:')
    value.append(city)

print(tuple(value))
