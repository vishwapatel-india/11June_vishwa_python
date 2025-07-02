print('========Welcome to KEndriya Vidhyalay===========')

sub1=int(input('Enter the marks of Sci:'))
sub2=int(input('Enter the marks of Maths:'))
sub3=int(input('Enter the marks of Eng:'))
sub4=int(input('Enter the marks of Hindi:'))

if sub1>=40 and sub2>=40 and sub3>=40 and sub4>=40: #parent condition

    total=sub1+sub2+sub3+sub4
    print("Total marks obtained=",total)

    per= total/4
    print("Percentage obtained=",per)

    if per>70:  #child condition
        print('Passed with first class distinction')
    elif per>60:
        print('passed with first class')
    elif per>50:
        print('Passed with second class')
    elif per>40:
        print('Passed')
else: 
    print("Failed!!!")

print("=====Best of luck for your bright future=====")


