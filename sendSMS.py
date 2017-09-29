# -*- coding: utf-8 -*-
import uuid
import json
import time
from aliyun import send_sms
try:
    import cPickle as pickle
except ImportError:
    import pickle


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
for info in data:
    name = info[0]
    tel = str(info[1])
    inTime = changeTime(info[2])

    __business_id = uuid.uuid1()
    params = json.dumps({"name": name, "time": inTime})
    sms_out = send_sms(__business_id, tel, "CSECL实验室", "SMS_100890067", params)
    status = json.loads(sms_out)["Code"]
    print status
    time.sleep(10)
