# -*- coding: utf-8 -*-
import uuid
import json
import time
from aliyun import send_sms
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


def sendSurplus(sms):
    SMSFail = list()
    for info in sms:
        code = info[0]
        name = info[1]
        tel = info[2]
        email = info[3]
        inTime = info[4]
        statusSMS = sendSms(name.encode('utf-8'), tel.encode('utf-8'),
                            inTime.encode('utf-8'), code.encode('utf-8'))
        print name.encode('utf-8'), tel.encode('utf-8'), code.encode('utf-8'), inTime.encode('utf-8'), statusSMS
        if statusSMS != "OK":
            SMSFail.append([code, name, tel, email, inTime])
        time.sleep(2)
    return SMSFail


with open(r'txt/sms.txt', 'rb') as f:
    sms = pickle.load(f)


if sms == list():
    SMSFail = list()
    print "------------NOTICE------------"
    print "短信上次已全部发送"
    print "------------OVER--------------"
else:
    SMSFail = sendSurplus(sms)
    print "------------NOTICE------------"
    print "短信此次未发送成功："
    for info in SMSFail:
        print info[0].encode('utf-8'), info[1].encode('utf-8'), info[2].encode('utf-8'),info[4].encode('utf-8')
    print "------------OVER--------------"


with open(r'txt/sms.txt', 'wb') as f:
    pickle.dump(SMSFail, f, True)

del sms
