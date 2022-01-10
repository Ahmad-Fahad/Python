import mysql.connector

link = mysql.connector.connect(host="localhost", user="root", password="", database="data_sql")
_cursor = link.cursor()

#_cursor.execute("CREATE DATABASE data_sql")




