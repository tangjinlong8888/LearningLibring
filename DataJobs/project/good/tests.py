import pymysql


conn = pymysql.connect('127.0.0.1','root','123456','spider',3306)
# conn = pymysql.connect('192.168.2.104','admin','123456','zl_db',3306)
cur = conn.cursor()
res = cur.execute('insert into dq_user values ("8888")')
conn.commit()
# res = cur.execute('select * from dq_user')
#搜取所有结果
results = cur.fetchall()
# print(results)
cur.close()
conn.close()

