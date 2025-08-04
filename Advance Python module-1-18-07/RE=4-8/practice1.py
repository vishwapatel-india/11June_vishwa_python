import re
mystr="This is python"

x=re.search("This",mystr)
print(x)

if x:
    print("Match Done")

else:
    print("Error")