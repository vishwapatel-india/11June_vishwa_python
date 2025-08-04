
import re
mystr="This is python"
#match function search different asked function
x=re.match("python",mystr)
print(x)

if x:
    print("Match Done")

else:
    print("Error")