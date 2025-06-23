sub1=int(input("Enter the marks of Sub1="))
sub2=int(input("Enter the marks of Sub2="))
sub3=int(input("Enter the marks of Sub3="))
sub4=int(input("Enter the marks of Sub4="))
sub5=int(input("Enter the marks of Sub5="))
sub6=int(input("Enter the marks of Sub6="))

total=(sub1+sub2+sub3+sub4+sub5+sub6)
print("The total marks obtained:",total)
per=total/6 
print("percentage obtained:",per)

if (sub1 and sub2 and sub3 and sub4 and sub5 and sub6 <=40):
    print("FAIL")

elif per>70:
    print("A grade with distinction")
elif per>60:
    print("A grade")
elif per>50:
    print("B grade")
elif per>40:
    print("C grade")
