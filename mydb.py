# Install Mysql on your computer
# https://dev.mysql.com/downloads/installer/
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python
# 
# 

import mysql.connector

dataBase = mysql.connector.connect(

    host = 'localhost',
    user = 'root',
    password = 'pass1212',

)

# prepare a cursor object 

cursorObject = dataBase.cursor()

#create a database
cursorObject.execute("CREATE DATABASE db_crm")

print("DATABASE Created sucessfully !..")




