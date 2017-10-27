# # -*- coding: utf-8 -*-
try:
    import cPickle as pickle
except ImportError:
    import pickle

with open(r'txt/sms.txt', 'rb') as f:
    sms = pickle.load(f)

print sms[0][4]
