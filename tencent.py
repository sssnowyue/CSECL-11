# -*- coding: utf-8 -*-
import json
import Qcloud.Sms.sms as SmsSender


class SendMes(object):
    appid = 1400044503
    appkey = "ef5a38a9397fce48d7b1565582c53273"
    nation_code = "86"
    templ_id = 46615
    sign = "CSECL实验室"
    extend = ""
    ext = ""

    def __init__(self, appid, appkey, nation_code, templ_id, sign, extend, ext):
        self.appid = appid
        self.appkey = appkey
        self.sender = SmsSender
        self.nation_code = nation_code
        self.templ_id = templ_id
        self.sign = sign
        self.extend = extend
        self.ext = ext

    def sendTwo(self, phone_number, params):

        # single_sender = SmsSender.SmsSingleSender(appid, appkey)
        single_sender = self.sender.SmsSingleSender(self.appid, self.appkey)

        result = single_sender.send_with_param(
            self.nation_code, phone_number, self.templ_id, params, self.sign, self.extend, self.ext)
        rsp = json.loads(result)

        return result
