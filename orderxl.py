# -*- coding: utf-8 -*-
import xlwt
import time
try:
    import cPickle as pickle
except ImportError:
    import pickle


def gettxt():
    with open('order.txt', 'rb') as f:
        d = pickle.load(f)
        return d


def changeTime(timestamp):
    # 转换成localtime
    time_local = time.localtime(timestamp)
    # 转换成新的时间格式
    return time.strftime("%Y-%m-%d %A %H:%M", time_local)


wb = xlwt.Workbook()
ws = wb.add_sheet('Sheet1')

title = [u"姓名", u"方向", u"手机号", u"面试预计时间", u"签名", u"实际到场时间"]
for i in range(len(title)):
    ws.write(0, i, title[i])


data = gettxt()
for y in range(len(data)):
    for x in range(4):
        if x == 4:
            ws.write(y + 1, x-1, changeTime(data[y][x]))
        elif x == 1:
            ws.write(y + 1, x + 1, data[y][x])
        elif x == 3:
            ws.write(y + 1, x - 2, data[y][x])
        elif x == 0:
            ws.write(y + 1, x, data[y][x])
        else:
            pass

wb.save('面试顺序表.xls')
