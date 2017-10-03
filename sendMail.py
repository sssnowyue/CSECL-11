# -*- coding: utf-8 -*-
import time
import smtplib
from email.mime.text import MIMEText
from email.header import Header
try:
    import cPickle as pickle
except ImportError:
    import pickle


def send(Sender, receiver, smtpObj, name, inTime):
    text = name + u'同学，你好！请于' + inTime + \
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


def changeTime(timestamp):
    # 转换成localtime
    time_local = time.localtime(timestamp)
    # 转换成新的时间格式
    return time.strftime("%Y-%m-%d %A %H:%M", time_local)


def gettxt():
    with open('order.txt', 'rb') as f:
        d = pickle.load(f)
        return d


data = gettxt()
sendFail1 = list()
sendFail = list()

Sender = u'sssnowyue@163.com'
AuthorizationCode = u'1123146105yuyue'
smtp_server = u'smtp.163.com'
smtpObj = smtplib.SMTP()
smtpObj.connect(smtp_server, 25)
smtpObj.login(Sender, AuthorizationCode)

for info in data:
    name = info[0]
    receiver = info[2]
    inTime = changeTime(info[4]).decode('utf-8')
    status = send(u'sssnowyue@163.com', receiver, smtpObj, name, inTime)
    print name.encode('utf-8'), receiver.encode('utf-8'), status
    time.sleep(2)
    if status == "Fail":
        sendFail1.append([name, receiver, inTime])

if sendFail1 == list():
    print "...................................."
    print "第一次发送全部成功！！！"
else:
    print "...................................."
    print "第一次发送失败重新发送中......"
    for info in sendFail1:
        name = info[0]
        receiver = info[1]
        inTime = info[2]
        status = send('sssnowyue@163.com', receiver, smtpObj, name, inTime)
        print name.encode('utf-8'), receiver.encode('utf-8'), status
        time.sleep(10)
        if status == "Fail":
            sendFail.append([name, receiver, inTime])
del sendFail1

if sendFail == list():
    print "...................................."
    print "第二次发送全部成功"
else:
    print "...................................."
    print "短信发送失败报名者："
    for info in sendFail:
        print info[0].encode('utf-8'), info[1].encode('utf-8'), info[2].encode('utf-8')
del sendFail

smtpObj.quit()
