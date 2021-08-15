
# 1.*
# 2.all categories
# 3.all categories and brand

from pymysql import *

conn = connect(host='localhost',port=3306,database='jing_dong',user='root',password='Mysql123!',charset='utf8')

cs1 = conn.cursor()

count = cs1.execute('select * from goods')

print(count)

result = cs1.fetchall()
print(result)


cs1.close()
conn.close()


