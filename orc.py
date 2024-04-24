#Oracle instant client" if u face error
'''
import cx_Oracle
con=cx_Oracle.connect("system/oracle@localhost")
if con!=None:
    print("connection established successfully")
    print("version",con.version)
else:
    print("connection is not established")

con.close()
'''


