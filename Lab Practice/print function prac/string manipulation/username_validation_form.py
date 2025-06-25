def registration_user():
    print('=======User Registration======')

    firstname=input('Enter your first name=').strip()
    print(firstname.lower())
    if not firstname:
        print('firstname cannot be empty!')
        return

    lastname=input('Enter last name=').strip()
    print(lastname.lower())
    if not lastname:
        print("lastname cannot be empty")
        return

    emailid=input('Enter email id:=').strip()
    print(emailid.lower())
    if not emailid:
        print("emailid cannor be empty")
        return

    password=input('Enter password=')
    confirm_password=input('Enter confirm password=')
    #print(password.alphanum())
    if not password:
        print('Password cannot be empty')
        return
    if len(password) < 8:
        print("Password cannot be less than 8")
        return
    if password != confirm_password:
        print('password do not match')
        return

    mobile_num=input("Enter your number").strip()
    #print(mobile_num.isdigit())
    if not mobile_num:
        print("Mobile_num cannot be empty")
        return
    if (mobile_num)==10:
        print("mobile_num cannot be less than 10 digit")
        return

    print("Registration Succesful!!!")

registration_user()