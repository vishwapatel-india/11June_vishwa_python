stdata={'id':101,
        'name':'vishu',
        'sub':'science'}
"""
print(stdata)
print(stdata['name'])
print(stdata.get('sub'))

print(stdata.keys)
print(stdata.values)

print(len(stdata)) #pair is counted
if 'name' in stdata:
    print("YES")
else:
    print('NO')

if 'vishu' in stdata.value():
    print('YEs')
else:
    print("NO")

for i in stdata.values():
    print(i)

for i in stdata.items():
    print(i)                   # gives both keys and values

for i,j in stdata.items():
    print(i,j)      # removes bracket
    print(f"key={i} and values={j}")"""

stdata['city']='Rajokt'
print(stdata)