#modifier are optional flag
#different modifier are used 

import re
str="This is vishwa!!"
"""x=re.findall("[A-Z]",str)
x=re.findall("[a-z]",str)
x=re.findall("[0-9]",str)
"""
x=re.findall("[A-Za-z. ]",str) #allows all upper and lower case and anything which is allowed
print(x)