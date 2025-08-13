import sqlite3

try:
    db=sqlite3.connect("new.db")
    print("Database created!!")
except Exception as e:
    print(e)

#table create
tbl_create="create table studinfo(id integer primary key autoincrement," 
"name text, city text)"

try:
    db.execute(tbl_create)
    print("Table created")

except Exception as e:
    print(e)

"""#insert table  #for dml query you compulsory need to commit the query
insert_data="insert into studinfo(name,city)values('vishwa','jamnagar'),('vishal','rjkt'),('harit','ahmd')"
try:
    db.execute(insert_data)
    db.commit()
    print("Data inserted")
except Exception as e:
    print(e)
"""

"""#update data
update_data="update studinfo set name='khushbu',city='bangalore' where id=1"
try:
    db.execute(update_data)
    db.commit()
    print("updation complete")
except Exception as e:
    print(e)
"""

"""#delete data
delete_data="delete from studinfo where id=2"
try:
    db.execute(delete_data)
    db.commit()
    print("Deleted successfully")
except Exception as e:
    print(e)
"""

#show data
cr=db.cursor()
show_data="select * from studinfo"
try:
    cr.execute(show_data)
    data=cr.fetchall()
    #data=cr.fetchone
    #data=cr.fetchmany
    #print(data)

    for i in data:
        print(i[1])
except Exception as e:
    print(e)