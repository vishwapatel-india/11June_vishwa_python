a=int(input("Enter a number:"))

if a<=1:
    print("The number is not a prime number")

elif a==2:
    print("prime number")

else:
    for i in range(2,a):
        if a % i==0:
            print("Not a prime number")
            break

        else:
            print("Prime number")
    
