a=int(input('Enter the value of A:'))
b=int(input('Enter the value of B:'))

if a!=0 and b!=0:
    if a>b: #max
        print('A is maxinmum',a*b)
    
    else a<b:  #min
        print("A is minimun", a-b)

else:
    print("ERROR!!!! Invalid Entry") 