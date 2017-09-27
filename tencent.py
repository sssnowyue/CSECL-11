# -*- coding: utf-8 -*-
import json
import Qcloud.Sms.sms as SmsSender


class SendMes(object):
    appid = 1400044503
    appkey = "ef5a38a9397fce48d7b1565582c53273"

    def __init__(self, appid, appkey):
        self.appid = appid
        self.appkey = appkey
        self.sender = SmsSender

    def sendOne(self, phone_numbers, templ_id, params):
        # multi_sender = SmsSender.SmsMultiSender(appid, appkey)
        multi_sender = self.sender.SmsMultiSender(self.appid, self.appkey)

        result = multi_sender.send_with_param(
            "86", phone_numbers, templ_id, params, "", "", "")
        rsp = json.loads(result)
        return result

    def sendTwo(self, phone_number, templ_id, params):

        # single_sender = SmsSender.SmsSingleSender(appid, appkey)
        single_sender = self.sender.SmsSingleSender(self.appid, self.appkey)

        result = single_sender.send_with_param(
            "86", phone_number, templ_id, params, "CSECL实验室", "", "")
        rsp = json.loads(result)

        return result
