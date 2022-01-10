import mysql.connector as c

link = c.connect(host="localhost", user="root", password="", database="experiment")

_cursor = link.cursor()


#_cursor.execute("CREATE DATABASE data_sql")

'''
_cursor.execute("SHOW DATABASES")

for i in _cursor:
	print(i)
	

_cursor.execute("SHOW TABLES")

for i in _cursor:
	print(i)

query = "INSERT INTO employee(name, dept, salary, email, designation) VALUES('PPP', 'ECE', 60000, 'ppp@gmail.com', 'Engineer')"
_cursor.execute(query)

query = "SELECT * FROM employee"
_cursor.execute(query)
for i in _cursor:
	print(i)



query  = "INSERT INTO employee(name, dept, email, designation) VALUES(%s, %s, %s, %s)" 
values = ("RRR", "ETE", "RRR@gmail.com", "Engineer")
_cursor.execute(query, values)



query  = "INSERT INTO employee(name, email) VALUES(%s, %s)" 
values = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]

_cursor.executemany(query, values)
link.commit()
print(_cursor.rowcount, "Record inserted")
print(f"Last Row id is {_cursor.lastrowid}")

'''
query = "SELECT * FROM employee"
_cursor.execute(query)
result = _cursor.fetchall()  #last inserted all
for i in result:
	print(i)
print(_cursor.fetchone()) #last insertted record

# link.commit : after insert, delete, update

