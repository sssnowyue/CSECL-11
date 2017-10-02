# -*- coding: utf-8 -*-
import xlwt
import MySQLdb

# 打开数据库连接
db = MySQLdb.connect(host="115.159.157.37", user="root",
                     db="csecl", passwd="ct-sch", port=3306,charset='utf8')

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 查询语句
sql = "SELECT `direct`,`name`,`sex`,`phone`,`qq`,`email`,`number`,`college`,`major`,`english_grade`,`math_grade`,`address` FROM application ORDER BY rand()"

# 执行SQL语句
cursor.execute(sql)

# 获取所有记录列表
results = cursor.fetchall()

wb = xlwt.Workbook()
ws1 = wb.add_sheet(u'程序')
ws2 = wb.add_sheet(u'前端')
ws3 = wb.add_sheet(u'产品')

title = [u"姓名", u"性别", u"手机号", u"QQ号", u"邮箱",
         u"学号", u"学院", u"专业", u"英语", u"数学", u"籍贯"]
for i in range(len(title)):
    ws1.write(0, i, title[i])
    ws2.write(0, i, title[i])
    ws3.write(0, i, title[i])

y1 = 1
y2 = 1
y3 = 1
for info in results:
    if info[0] == u"程序":
        for x in range(11):
            if x == 8 or x == 9:
                ws1.write(y1, x, info[x + 1])
            elif x == 1:
                if info[x + 1] == 1:
                    ws1.write(y1, x, u"男")
                else:
                    ws1.write(y1, x, u"女")
            else:
                ws1.write(y1, x, info[x + 1])
        y1 += 1
    elif info[0] == u"前端":
        for x in range(11):
            if x == 8 or x == 9:
                ws2.write(y2, x, info[x + 1])
            elif x == 1:
                if info[x + 1] == 1:
                    ws2.write(y2, x, u"男")
                else:
                    ws2.write(y2, x, u"女")
            else:
                ws2.write(y2, x, info[x + 1])
        y2 += 1
    elif info[0] == u"产品":
        for x in range(11):
            if x == 8 or x == 9:
                ws3.write(y3, x, info[x + 1])
            elif x == 1:
                if info[x + 1] == 1:
                    ws3.write(y3, x, u"男")
                else:
                    ws3.write(y3, x, u"女")
            else:
                ws3.write(y3, x, info[x + 1])
        y3 += 1
    else:
        print "数据库内方向字段不符合项："
        print info[1]

wb.save('基本信息.xls')
