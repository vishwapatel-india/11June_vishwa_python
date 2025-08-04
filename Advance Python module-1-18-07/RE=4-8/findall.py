import re
mystr="This is python"
#search function search different asked function
x=re.findall("This",mystr)
print(x)

if x:
    print("Match Done")

else:
    print("Error")