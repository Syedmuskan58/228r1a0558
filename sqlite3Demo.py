'''import sqlite3
con=sqlite3.connect("mydatabase.db")
cur=con.cursor()
#cur.execute("create table if not exists  students(name varchar(50),rollno varchar(50),sec varchar(50))")
#cur.execute('insert into students values("muskan","101","A")')
#cur.execute('insert into students values("ramesh","ID512","B")')
#cur.execute('insert into students values("somesh","ID513","C")')
#cur.execute('delete from students where name="muskan"')
cur.execute('update students set name="mushu" where rollno="ID512" ')
x=cur.execute('select *from students')
print(x.fetchall())
x.cur.execute("show tables")
con.commit()
print(x)'''
print