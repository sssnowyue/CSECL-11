# -*- coding: utf-8 -*-
import time
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL
try:
    import cPickle as pickle
except ImportError:
    import pickle


def sendEmail(Sender, receiver, smtpObj, name, code, inTime):
    text = name + u'同学，你好！你已成功报名互联网创新实验室CSECL，你的编号为' + code + u'（请牢记编号），请于' + inTime + \
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
    text = name + '同学，你好！你已成功报名互联网创新实验室CSECL，你的编号为' + code + '（请牢记编号），请于' + inTime + \
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


def sendSurplus(mail, smtpQ, smtpObj):
    MailFail = list()
    for info in mail:
        code = info[0]
        name = info[1]
        tel = info[2]
        email = info[3]
        inTime = info[4]
        statusEmail = sendQEmail('1123146105@qq.com',
                                 email.encode('utf-8'), smtpQ, name.encode('utf-8'), code.encode('utf-8'), inTime.encode('utf-8'))
        if statusEmail != "OK":
            statusEmail = sendEmail(u'sssnowyue@163.com',email, smtpObj, name, code, inTime)
            if statusEmail != "OK":
                MailFail.append([code, name, tel, email, inTime])
                print name.encode('utf-8'), email.encode('utf-8'), code.encode('utf-8'), inTime.encode('utf-8'), statusEmail
            else:
                print name.encode('utf-8'), email.encode('utf-8'), code.encode('utf-8'), inTime.encode('utf-8'), statusEmail
        else:
            print name.encode('utf-8'), email.encode('utf-8'), code.encode('utf-8'), inTime.encode('utf-8'), statusEmail
        time.sleep(4)
    return MailFail

with open(r'txt/mail.txt', 'rb') as f:
    mail = pickle.load(f)

#163 login
Sender = u'sssnowyue@163.com'
AuthorizationCode = u'1123146105yuyue'
smtp_server = u'smtp.163.com'
smtpObj = smtplib.SMTP()
smtpObj.connect(smtp_server, 25)
smtpObj.login(Sender, AuthorizationCode)

#qq login
smtpQ = SMTP_SSL('smtp.qq.com')
smtpQ.set_debuglevel(0)
smtpQ.ehlo('smtp.qq.com')
smtpQ.login('1123146105', 'voxuytjaoyfpgegc')

if mail == list():
    MailFail = list()
    print "------------NOTICE------------"
    print "邮箱上次已全部发送"
    print "------------OVER--------------"
else:
    MailFail = sendSurplus(mail, smtpQ, smtpObj)
    print "------------NOTICE------------"
    print "邮箱此次未发送成功："
    for info in MailFail:
        print info[0].encode('utf-8'), info[1].encode('utf-8'), info[2].encode('utf-8'),info[4].encode('utf-8')
    print "------------OVER--------------"

with open(r'txt/mail.txt', 'wb') as f:
    pickle.dump(MailFail, f, True)

del mail
