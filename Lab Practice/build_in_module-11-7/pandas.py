import pandas

stdata={
    "id":[1,2,3,4,5],
    "name":['vishu','vishal','vishwa','shivansh','harit'],
    "city":['rjkt','ahmd','jmanagar','brd','morbi']
    }

data=pandas.DataFrame(stdata)
print(data)