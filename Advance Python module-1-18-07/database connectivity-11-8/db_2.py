import sqlite3
try:
    db=sqlite3.connect("Practice.db")
    print("Db created")
except Exception as e:
    print(e)

#create table
table="create table product(pid integer primary key autoincrement,pname text,qty integer)"
try:
    db.execute(table)
    print("Table created")
except Exception as e:
    print(e)

#insert data
"""insert="insert into product(pname,qty)values ('shampoo',15),('hair mask',5),('serum',5),('moisturizer',4),('face toner',2)"
try:
    db.execute(insert)
    db.commit()
    print("Data added successfully")
except Exception as e:
    print(e)
"""
#update table
"""update="update product set pname='conditioner',qty=8 where pid=4"
try:
    db.execute(update)
    db.commit()
    print("Updation successful")
except Exception as e:
    print(e)
"""
#show data
show=db.cursor()
show_data="select * from product"
try:
    show.execute(show_data)
    data=show.fetchall()
    
    for i in data:
        print(i[2])

except Exception as e:
    print(e)
