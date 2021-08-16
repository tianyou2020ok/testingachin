# 1.*
# 2.all categories
# 3.all categories and brand

from pymysql import *

conn = connect(host='localhost',port=3306,database='jing_dong',user='root',password='Mysql123!',charset='utf8')

cs1 = conn.cursor()


print('1.查询所有数据')
print('1.查询所有种类')
print('1.查询所有种类和品牌')
print('4.退出')
select = int(input('请输入'))

while True:
    #
    if select == 1:
        count = cs1.execute('select * from goods')

        print('共有d%行数据' %count)
        result = cs1.fetchall()
        print(result)

    #
    if select == 2:
        count = cs1.execute('select * from goods')

        print('共有d%行数据' %count)
        result = cs1.fetchall()
        print(result)

    #
    if select == 3:
        count = cs1.execute('select * from goods')

        print('共有d%行数据' %count)
        result = cs1.fetchall()
        print(result)

    #
    if select == 4:
        break

    if select != 1 or select != 2 or select != 3 or select != 4:
        print("输入有误，请重新输入")

cs1.close()
conn.close()

