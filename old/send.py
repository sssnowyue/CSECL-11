# -*- coding: utf-8 -*-
import xlrd
import uuid
import json
import time
from aliyun import send_sms
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL
try:
    import cPickle as pickle
except ImportError:
    import pickle


def sendSms(name, tel, inTime, code):
    __business_id = uuid.uuid1()
    params = json.dumps({"name": name, "time": inTime, "code": code})
    sms_out = send_sms(__business_id, tel, "CSECL实验室", "SMS_103190005", params)
    status = json.loads(sms_out)["Code"]
    return status


def sendEmail(Sender, receiver, smtpObj, name, code, inTime):
    text = name + u'同学，你好！，你的编号为' + code + u'（请牢记编号），请于' + inTime + \
        u'到13教509参加面试，请提前15分钟到场，收到后请在［CSECL-11招新］群（672099668）查看面试详尽并在群内回复（11+方向+姓名+已收到面试通知），谢谢！'
    msg = MIMEText(text, 'plain', 'utf-8')
    msg['Subject'] = Header('互联网创新实验室通知', 'utf-8')
    msg['From'] = Sender
    msg['To'] = receiver
    try:
        smtpObj.sendmail(Sender, receiver, msg.as_string())
        return "OK"
    except smtplib.SMTPException:
        return "Fail"


def sendQEmail(Sender, receiver, smtpQ, name, code, inTime):
    text = name + '同学，你好！，你的编号为' + code + '（请牢记编号），请于' + inTime + \
        '到13教509参加面试，请提前15分钟到场，收到后请在［CSECL-11招新］群（672099668）查看面试详尽并在群内回复（11+方向+姓名+已收到面试通知），谢谢！'
    msg = MIMEText(text, 'plain', 'utf-8')
    msg['Subject'] = Header('互联网创新实验室通知', 'utf-8')
    msg['From'] = Sender
    msg['To'] = receiver
    try:
        smtpQ.sendmail(Sender, receiver, msg.as_string())
        return "OK"
    except:
        return "Fail"


Sender = u'sssnowyue@163.com'
AuthorizationCode = u'1123146105yuyue'
smtp_server = u'smtp.163.com'
smtpObj = smtplib.SMTP()
smtpObj.connect(smtp_server, 25)
smtpObj.login(Sender, AuthorizationCode)

# QQ email login of ssl
smtpQ = SMTP_SSL('smtp.qq.com')
smtpQ.set_debuglevel(0)
smtpQ.ehlo('smtp.qq.com')
smtpQ.login('1123146105', 'voxuytjaoyfpgegc')


data = xlrd.open_workbook('面试顺序表.xls')

table1 = data.sheet_by_name(u'程序')
table2 = data.sheet_by_name(u'前端')
table3 = data.sheet_by_name(u'产品')


SMSFail0 = list()
EmailFail0 = list()
SMSFail = list()
EmailFail = list()

for table in [table1, table2, table3]:
    for rownum in range(1, table.nrows):
        oneInfo = table.row_values(rownum)
        code = oneInfo[0]
        name = oneInfo[1]
        tel = oneInfo[2]
        email = oneInfo[3]
        inTime = oneInfo[4]
        # sendSMS
        statusSMS = sendSms(name.encode('utf-8'),
                            tel.encode('utf-8'), inTime.encode('utf-8'), code.encode('utf-8'))
        print name.encode('utf-8'), tel.encode('utf-8'), code.encode('utf-8'), inTime.encode('utf-8'), statusSMS
        if statusSMS != "OK":
            SMSFail0.append([name, tel, inTime, code])
        #sendEmail
        statusEmail = sendEmail(u'sssnowyue@163.com',
                                email, smtpObj, name, code, inTime)
        print name.encode('utf-8'), email.encode('utf-8'), code.encode('utf-8'), inTime.encode('utf-8'), statusEmail
        if statusEmail == "Fail":
            EmailFail0.append([name.encode(
                'utf-8'), email.encode('utf-8'), code.encode('utf-8'), inTime.encode('utf-8')])
        time.sleep(8)


if SMSFail0 == list():
    print "...................................."
    print "短信第一次发送全部成功！！！"
else:
    print "...................................."
    print "短信第一次发送失败重新发送中......"
    for info in SMSFail0:
        statusSMS = sendSms(info[0].encode(
            'utf-8'), info[1].encode('utf-8'), info[2].encode('utf-8'), info[3].encode('utf-8'))
        print info[0].encode('utf-8'), info[1].encode('utf-8'), info[2].encode('utf-8'), info[3].encode('utf-8'), statusSMS
        time.sleep(8)
        if statusSMS != "OK":
            SMSFail.append(
                [info[0].encode('utf-8'), info[1].encode('utf-8'), info[2].encode('utf-8')])

if EmailFail0 == list():
    print "...................................."
    print "163邮箱发送全部成功！！！"
else:
    print "...................................."
    print "QQ邮箱发送中......"
    for info in EmailFail0:
        statusEmail = sendQEmail('1123146105@qq.com',
                                 info[1], smtpQ, info[0], info[2], info[3])
        print info[0], info[1], info[2], info[3], statusEmail
        time.sleep(8)
        if statusEmail == "Fail":
            EmailFail.append([info[0], info[1], info[2], info[3]])

print "...................................."
print "短信发送失败："
for info in SMSFail:
    print info[0], info[1], info[2]

print "...................................."
print "邮箱发送失败："
for info in EmailFail:
    print info[0], info[1], info[2], info[3]

with open(r'txt/sms.txt', 'wb') as f:
    pickle.dump(SMSFail, f, True)
with open(r'txt/mail.txt', 'wb') as f:
    pickle.dump(EmailFail, f, True)

del table
del SMSFail0
del EmailFail0
del SMSFail
del EmailFail
