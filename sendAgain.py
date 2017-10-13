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

with open(r'txt/sms.txt', 'rb') as f:
    sms = pickle.load(f)
