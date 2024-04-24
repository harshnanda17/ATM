'''
import sqlite3
conn = sqlite3.connect('college.db')
c = conn.cursor()

def create_table():
    c.execute("create table if not exists Emp(EmpId text,EmpName text,EmpJob text,Salary Integer)")

def data_entry():
    c.execute("insert into Emp values('E001','rishi','student',2000)")
    conn.commit()
    c.close()
    conn.close()
#create_table()
data_entry()


#2: input by user
 
#dynamic data entry
import sqlite3
conn = sqlite3.connect('college.db')
c = conn.cursor()

def dynamic_data_entry():
    eid = input("please enter ur Emp id")
    ename = input("please enter ur name")
    ejob = input("please enter ur job")
    salary = int(input("please enter ur salary"))
    c.execute("insert into Emp(EmpId ,EmpName ,EmpJob ,Salary)VALUES(?,?,?,?)",(eid, ename, ejob, salary))
    conn.commit()

dynamic_data_entry()


#3
import sqlite3

conn=sqlite3.connect('college.db')
c = conn.cursor()
def read_from_db():
    c.execute('Select * From Emp')
    data = c.fetchall()
    #print(data)
    for row in data:
        print(row)
def read_from_db_oncondition():
    c.execute('Select * FROM Emp Where Salary > 4500')
    data = c.fetchall()
    for row in data:
        print(row)
#read_from_db()
read_from_db_oncondition()


#4
import sqlite3

conn = sqlite3.connect('college.db')
c = conn.cursor()


def update_in_db():
     c.execute('udate Emp set EmpName = "Dhoni" where EmpId = "E001" ')
     conn.commit()

     c.execute('SELECT * FROM Emp')
     data = c.fetchall()
     [print(row) for row in data]

def delete_from_db():
    c.execute('DELETE FROM Emp where EmpId = "E001" ')
    conn.commit()
    c.execute('SELECT * FROM Emp')
    data = c.fetchall()
    print(data)

#update_in_db()
delete_from_db()


#this prg to check the version of mysql
import pymysql
con=pymysql.connect(host="localhost",user="root",passwd="")
myCursor=con.cursor()
myCursor.execute("select version()")
v=myCursor.fetchone()
print("the mysql version is ",v)

#1

import pymysql

con=pymysql.connect(host="localhost",user="root",passwd="",db="college")
myCursor=con.cursor()

sql="""Insert into Emp (Empid,Empname,Empjob,Empsalary)Value('E003','Shweta','Manager',6000)"""
myCursor.execute(sql)
con.commit()
print("record is inserted")
con.close()

#2
#this prg to update the record in table

import pymysql

con=pymysql.connect(host="localhost",user="root",passwd="",db="college")

myCursor=con.cursor()
sql="""Update Emp set Empname='Hardik'
where Empid='E003' """
myCursor.execute(sql)
con.commit()
print("record is updated")

con.close()
 

#3
#this prg to update the record in table
import pymysql

con=pymysql.connect(host="localhost",user="root",passwd="",db="college")

myCursor=con.cursor()
sql="Delete From Emp where Empid='E003' "

myCursor.execute(sql)
con.commit()
print("record is Deleted")
con.close()


#4

#1:this prg to retrieve all records from table
import pymysql

con=pymysql.connect(host="localhost",user="root",passwd="",db="college")

myCursor=con.cursor()
sql="Select * from Emp"
myCursor.execute(sql)
print(myCursor.fetchall())
con.close()
'''

#2:
#this prg to retrieve all records from table
import pymysql

con=pymysql.connect(host="localhost",user="root",passwd="",db="college")

myCursor=con.cursor()
sql="Select * from Emp"
myCursor.execute(sql)
result=myCursor.fetchall()

for row in result:
    Empid=row[0]
    Empname=row[1]
    Empjob=row[2]
    salary=row[3]
    print("Id=%s ,Name=%s ,Job=%s ,Salary=%d"%(Empid,Empname,Empjob,salary))

con.close()

