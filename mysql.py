# -*- coding: utf-8 -*-
import MySQLdb
try:
    import cPickle as pickle
except ImportError:
    import pickle

# 打开数据库连接
db = MySQLdb.connect(host="115.159.157.37", user="root",
                     db="csecl", passwd="ct-sch", port=3306)

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 查询语句
sql = "SELECT `name`,`phone`,`email`,`direct` FROM application ORDER BY rand()"

# 执行SQL语句
cursor.execute(sql)

# 获取所有记录列表
results = cursor.fetchall()


save = list()
p = 1
# 批次开始时间（晚上，次日上午，次日下午）
t1 = 1508497200
t2 = 1508547600
t3 = 1508565600
# 每批人数
n1 = 40
n2 = 40
# 每人面试时长
onetime = 10 * 60
for re in results:
    if p < n1 + 1:
        t = t1 + (p - 1) * onetime
        re = list(re)
        re.append(t)
        save.append(re)
        p += 1

    elif n1 < p < n1 + n2 + 1:
        t = t2 + (p - n1 - 1) * onetime
        re = list(re)
        re.append(t)
        save.append(re)
        p += 1
    else:
        t = t3 + (p - n1 - n2 - 1) * onetime
        re = list(re)
        re.append(t)
        save.append(re)
        p += 1

with open('order.txt', 'wb') as f:
    pickle.dump(save, f, True)
