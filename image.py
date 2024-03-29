"""
存取二进制文件演示
"""

import pymysql

# 连接数据库
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='123456',
                     database='test',
                     charset='utf8')

# 生成游标对象 (操作数据库，执行sql语句)
cur = db.cursor()

# 存储图片
# with open('lyf.jpg','rb') as f:
#     data = f.read()
#
# try:
#     sql="insert into image values(1,%s,%s);"
#     cur.execute(sql,['lyf.jpg',data])
#     db.commit()
# except:
#     db.rollback()

# 读取图片
sql="select filename,img from image where filename='dlrb.jpg';"
cur.execute(sql)
data = cur.fetchone() # (filename,img)
with open(data[0],'wb') as f:
    f.write(data[1])


# 关闭游标和数据库连接
cur.close()
db.close()