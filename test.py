# -*- coding: utf-8 -*-
try:
    import cPickle as pickle
except ImportError:
    import pickle


def gettxt():
    with open('order.txt', 'rb') as f:
        d = pickle.load(f)
        return d

data = gettxt()

print type(data[0][1])