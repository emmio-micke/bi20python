import mysql.connector

mydb = mysql.connector.connect(
    host="remotemysql.com",  # your host, localhost for your local db
    user="AybEFDBRkG",       # username
    password="pbNAmdostq",   # password
    database="AybEFDBRkG"
)

mycursor = mydb.cursor()

mycursor.execute("show databases")

for db in mycursor:
    print(db)

# print(mydb)
