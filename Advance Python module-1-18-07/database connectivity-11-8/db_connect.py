import sqlite3

try:
    db=sqlite3.connect("temp.db")
    print("Database created!!")
except Exception as e:
    print(e)
    