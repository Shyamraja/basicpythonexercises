import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="oamklinux2019"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE myexercise")

