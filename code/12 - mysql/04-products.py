import mysql.connector

mydb = mysql.connector.connect(
    host="remotemysql.com",  # your host, localhost for your local db
    user="AybEFDBRkG",       # username
    password="pbNAmdostq",   # password
    database="AybEFDBRkG"
)

mycursor = mydb.cursor(dictionary=True)

sql = """
SELECT p.productName, p.MSRP, pl.textDescription
FROM products p
  JOIN productlines pl ON p.productline = pl.productline
ORDER BY p.MSRP DESC
LIMIT 10
"""

mycursor.execute(sql)

products_result = mycursor.fetchall()

for product in products_result:
    print(product)
