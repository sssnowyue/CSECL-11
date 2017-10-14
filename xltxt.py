# -*- coding: utf-8 -*-
import xlrd
try:
    import cPickle as pickle
except ImportError:
    import pickle

info = list()
# read xl
data = xlrd.open_workbook('面试顺序表.xls')

table1 = data.sheet_by_name(u'程序')
table2 = data.sheet_by_name(u'前端')
table3 = data.sheet_by_name(u'产品')

for table in [table1, table2, table3]:
    for rownum in range(1, table.nrows):
        oneInfo = table.row_values(rownum)
        info.append(oneInfo)
# write to txt
with open(r'txt/sms.txt', 'wb') as f:
    pickle.dump(info, f, True)
with open(r'txt/mail.txt', 'wb') as f:
    pickle.dump(info, f, True)

with open(r'txt/sms.txt', 'rb') as f:
    sms = pickle.load(f)
with open(r'txt/mail.txt', 'rb') as f:
    mail = pickle.load(f)
print "------------NOTICE------------"
print "SMS to TXT:"
print sms
print "------------OVER--------------"
print "------------NOTICE------------"
print "Mail to TXT:"
print mail
print "------------OVER--------------"