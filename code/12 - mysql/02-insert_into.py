import mysql.connector

mydb = mysql.connector.connect(
    host="remotemysql.com",  # your host, localhost for your local db
    user="AybEFDBRkG",       # username
    password="pbNAmdostq",   # password
    database="AybEFDBRkG"
)

mycursor = mydb.cursor()

sql = "INSERT INTO `AybEFDBRkG`.`customers` (`customerNumber`, `customerName`, `contactLastName`, `contactFirstName`, `phone`, `addressLine1`, `city`, `country`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

values = ('500', 'Kalles gatukök', 'Svensson', 'Karl',
          '12345', 'Stortorget 4', 'Norrköping', 'Sweden')
mycursor.execute(sql, values)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

# print(mydb)
