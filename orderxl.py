# -*- coding: utf-8 -*-
import xlwt
import MySQLdb

db = MySQLdb.connect(host="115.159.157.37", user="root",
                     db="csecl", passwd="ct-sch", port=3306, charset='utf8')
cursor = db.cursor()
sql = "SELECT `direct`,`name`,`phone`,`email` FROM application ORDER BY id asc"
cursor.execute(sql)
results = cursor.fetchall()

wb = xlwt.Workbook()
ws1 = wb.add_sheet(u'程序')
ws2 = wb.add_sheet(u'前端')
ws3 = wb.add_sheet(u'产品')

title = [u"编号",u"姓名",  u"手机号",u"邮箱", u"面试预计时间", u"签名", u"实际到场时间"]
for i in range(len(title)):
    ws1.write(0, i, title[i])
    ws2.write(0, i, title[i])
    ws3.write(0, i, title[i])

y1 = 1
y2 = 1
y3 = 1
for info in results:
    if info[0] == u"程序":
        for x in range(4):
            if x==0:
                code = "A" + str(y1)
                ws1.write(y1, x, code.decode('utf-8'))
            else:
                ws1.write(y1, x, info[x])
        y1 += 1
    elif info[0] == u"前端":
        for x in range(4):
            if x==0:
                code = "B" + str(y2)
                ws2.write(y2, x, code.decode('utf-8'))
            else:
                ws2.write(y2, x, info[x])
        y2 += 1
    elif info[0] == u"产品":
        for x in range(4):
            if x==0:
                code = "C" + str(y3)
                ws3.write(y3, x, code.decode('utf-8'))
            else:
                ws3.write(y3, x, info[x])
        y3 += 1
    else:
        print "数据库内方向字段不符合项："
        print info[1],info[2]

wb.save('面试顺序表.xls')
