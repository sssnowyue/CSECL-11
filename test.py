try:
    import cPickle as pickle
except ImportError:
    import pickle
with open('order.txt', 'rb') as f:
    try:
        d = pickle.load(f)
        print d
    except EOFError:
        print "jjjj"
