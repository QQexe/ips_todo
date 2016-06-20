import sqlite3
con = sqlite3.connect('todo.db')
con.execute("CREATE TABLE todo (id INTEGER PRIMARY KEY, task char(100) NOT NULL, status bool NOT NULL)")
con.execute("INSERT INTO todo (task,status) VALUES ('Open the door',1)")
con.execute("INSERT INTO todo (task,status) VALUES ('Get on the floor',1)")
con.execute("INSERT INTO todo (task,status) VALUES ('Everybody walk the dinosaur',1)")
con.execute("INSERT INTO todo (task,status) VALUES ('Whatever',1)")
con.commit()
