class studinfo: #ckass is collection of data member and function
    stid=12
    stnm="Vishwa"

    def func(self):
        print("This is studinfo")

    def sum(self,a,b):
        print("Sum:",a+b)

st=studinfo() #object of class
print("ID:",st.stid)
print("Name:",st.stnm)
st.func()
st.sum(12,45)

