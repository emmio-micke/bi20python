import mysql.connector

mydb = mysql.connector.connect(
    host="remotemysql.com",  # your host, localhost for your local db
    user="AybEFDBRkG",       # username
    password="pbNAmdostq",   # password
    database="AybEFDBRkG"
)

#mycursor = mydb.cursor()
mycursor = mydb.cursor(dictionary=True)

sql = "SELECT * \
        FROM customers \
        WHERE country = 'USA' \
        ORDER BY customerName \
        LIMIT 5"

sql = """
SELECT * FROM customers
WHERE country = 'USA'
ORDER BY customerName
LIMIT 5
"""

mycursor.execute(sql)

myresult = mycursor.fetchall()

for customer in myresult:
    #    print(customer[1])
    print(customer["customerName"])

# print(mydb)
