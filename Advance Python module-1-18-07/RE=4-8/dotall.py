import re

str="Hello Vishwa"
#x=re.findall("Vi...a",str) #length should be same as in input
x=re.findall("Hello|Hyy",str)
print(x)

#if matches it will whole word and in error returns blank list