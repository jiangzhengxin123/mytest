# -*- coding: UTF-8 -*-

#pip install impyla==0.15a1



from impala.dbapi import connect
conn = connect(host='192.168.234.128', port=10000, auth_mechanism='PLAIN', user='root', password='cloudera', database='czl')
cursor=conn.cursor()
cursor.execute('select * from stu_class')
data=cursor.fetchall()
data_true=[]
for i in data: data_true.append(list(i))
print(data_true)
cursor.close()
conn.close()








