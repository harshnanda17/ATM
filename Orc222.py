#1
'''
import cx_Oracle
con=cx_Oracle.connect("system/oracle@localhost")
q="create table Emp11(EmpId varchar2(10),EmpName varchar2(10),\
EmpJob varchar2(10),Salary number)"
c=con.cursor()
c.execute(q)

print("table created successfully")


#2

import cx_Oracle
con=cx_Oracle.connect("system/oracle@localhost")

q="insert into emp11 values('E001','Lata','trainer',5000)"
cursor=con.cursor()

cursor.execute(q)
con.commit()  #it is mandatory for DML
#DML:- data mainipulation language
print("record is inserted successfully")


#3

import cx_Oracle
con=cx_Oracle.connect("system/oracle@localhost")
cursor=con.cursor()
while True:
    EmpId=input("please enter ur EmpID")
    EmpName=input("please enter ur Name")
    EmpJob=input("please enter ur Job")
    Salary=int(input("please enter ur Salary"))
    query="insert into emp11 values('%s','%s','%s',%d)"
    cursor.execute(query %(EmpId,EmpName,EmpJob,Salary))
    con.commit()    #it is mandatory for DML
    print("record is inserted successfully")
    option=input("do you want to insert one more record[Yes|No]")
    if option == "No":
        break


#4
import cx_Oracle
con=cx_Oracle.connect("system/oracle@localhost")
cursor=con.cursor()

query="insert into emp11 values (:EmpId,:EmpName,:EmpJob,:Salary)"

records=[('E007','Dev','Student',2000),('E008','shiv','manager',8000),('E009','lata','admin',9000)]

cursor.executemany(query,records)
con.commit()  #IT IS MANDATORY FOR DML
print("record is inserted successfully")



#5
import cx_Oracle
con=cx_Oracle.connect("system/oracle@localhost")
cursor=con.cursor()

increment=int(input("pls enter increment salary"))
salary_range=int(input("pls enter salary range"))
query="update emp11 set salary=salary+%d where salary < %d"
cursor.execute(query %(increment,salary_range))
con.commit()  #it is mandatory for DML
print("record is updated successfully")
 


#6
import cx_Oracle
con=cx_Oracle.connect("system/oracle@localhost")
cursor=con.cursor()

cutoff=int(input("pls enter the cutoff salary"))
query="delete from emp11 where salary > %d"
cursor.execute(query %(cutoff))
con.commit()   #it is mandatory for DML
print("record is deleted successfully")
'''



