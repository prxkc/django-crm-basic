# install mysql
# pip install mysql
# pip install mysql-connector

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = ''
)

#prepare cursor object

cursorObject = dataBase.cursor()

#create database
cursorObject.execute("create database elderco")

print("[+] Database creation complete!")