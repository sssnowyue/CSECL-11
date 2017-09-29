# -*- coding: utf-8 -*-
import MySQLdb

# 打开数据库连接
db = MySQLdb.connect(host="115.159.157.37", user="root",
                     db="csecl", passwd="ct-sch", port=3306)

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 查询语句
sql = "SELECT `name`,`phone` FROM application ORDER BY rand()"

# 执行SQL语句
cursor.execute(sql)

# 获取所有记录列表
results = cursor.fetchall()

print results
print list(results)

# for row in results:
#     name = row[0]
#     tel = row[1]
#     print name,tel
