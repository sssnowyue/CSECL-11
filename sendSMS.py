# -*- coding: utf-8 -*-
import uuid
import json
import time
import MySQLdb
from aliyun import send_sms

db = MySQLdb.connect(host="115.159.157.37", user="root",
                     db="csecl", passwd="ct-sch", port=3306)
cursor = db.cursor()
sql = "SELECT * FROM application"
cursor.execute(sql)
results = cursor.fetchall()

timestamp = 1506684300
# 转换成localtime
time_local = time.localtime(timestamp)
# 转换成新的时间格式
dt = time.strftime("%Y-%m-%d %A %H:%M", time_local)


name = "于越"
inTime = dt
tel = str(13975659747)

__business_id = uuid.uuid1()
params = json.dumps({"name": name, "time": inTime})
sms_out = send_sms(__business_id, tel, "CSECL实验室", "SMS_100890067", params)
status = json.loads(sms_out)["Code"]
