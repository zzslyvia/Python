#coding=utf-8

import pymysql



conn = pymysql.connect(user="root",passwd="root",host="localhost",db="test1")

cur = conn.cursor()

cur.execute("SELECT * FROM user")

for r in cur:
    print("row_number:", (cur.rownumber))

    print("name:"+str(r[0])+"password:"+str(r[1]))

cur.close()

conn.close()









