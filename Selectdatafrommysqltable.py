import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="oamklinux2019",
  database="myexercise"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT name, address FROM students")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)
