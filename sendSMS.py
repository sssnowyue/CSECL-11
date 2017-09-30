# -*- coding: utf-8 -*-
import uuid
import json
import time
from aliyun import send_sms
try:
    import cPickle as pickle
except ImportError:
    import pickle


def sendSms(name, tel, inTime):
    __business_id = uuid.uuid1()
    params = json.dumps({"name": name, "time": inTime})
    sms_out = send_sms(__business_id, tel, "CSECL实验室", "SMS_100890067", params)
    status = json.loads(sms_out)["Code"]
    return status


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
for info in data:
    name = info[0]
    tel = str(info[1])
    inTime = changeTime(info[4])
    status = sendSms(name, tel, inTime)
    print name,tel,"OK"
    time.sleep(10)
    if status != "OK":
        sendFail1.append([name, tel, inTime])

if sendFail1 == list():
    print "第一次发送全部成功！！！"
else:
    for info in sendFail1:
        name = info[0]
        tel = str(info[1])
        inTime = changeTime(info[4])
        status = sendSms(name, tel, inTime)
        print name,tel,"OK"
        time.sleep(10)
        if status != "OK":
            sendFail.append([name, tel, inTime])

if sendFail == list():
    print "第二次发送全部成功"
else:
    print "短信发送失败报名者："
    for info in sendFail:
        print info[0], info[2], str(info[1]), changeTime(info[3])
