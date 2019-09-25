import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="oamklinux2019",
  database="myexercise"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE students (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
