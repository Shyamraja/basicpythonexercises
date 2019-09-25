import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="oamklinux2019",
  database="myexercise"
)

mycursor = mydb.cursor()

sql = "INSERT INTO students (name, address) VALUES (%s, %s)"
val = ("SAMBHOO", "Kotkantie 21")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "RECORDS inserted.")