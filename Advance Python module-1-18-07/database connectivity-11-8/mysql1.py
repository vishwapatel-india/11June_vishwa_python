import pymysql
try:
    v=pymysql.connect(host='localhost',user='root',password='',database='morningdb')
    print("DB connected")
except Exception as e:
    print(e)


cr=v.cursor()
table="create table studinfo(id integer primary key auto_increment, name text, city text)"
try:
    cr.execute(table)
    print("Table created")
except Exception as e:
    print(e)

#insert data
"""insert="insert into studinfo(name,city)values ('vishwa','rajkot'),('vishal','rajkot'),('harit','jamnagar')"

try:
    cr.execute(insert)
    v.commit()
    print("Record inserted")
except Exception as e:
    print(e)
"""
#update data
update= "update studinfo set name='khushbu',city='banglore' where id=3" 
try:
    cr.execute(update)
    v.commit()
    print("Record inserted")
except Exception as e:
    print(e)
