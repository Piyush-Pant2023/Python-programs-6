import mysql.connector as sqltor
mycin=sqltor.connect(host="localhost",user="root",password="1234",database="pp")
if mycin.is_connected():
    print("connected sucessfully")