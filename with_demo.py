'Teach in-detail how the with-statement works'

# How to open and close files -- TheOldWay(tm)

f = open('notes/hamlet.txt')
try:
    play = f.read()
    print len(play)
finally:
    f.close()

# How to open and close files -- TheNewWay(tm)

with open('notes/hamlet.txt') as f:
    play = f.read()
    print len(play)

# How to make locks ##########################

import threading

printer_lock = threading.Lock()


# How to use locks -- TheOldWay(tm)

printer_lock.acquire()          # This blocks until the lock is available
try:
    print 'Critical section 1'
    print 'Critical section 2'
finally:
    printer_lock.release()


# How to use locks -- TheNewWay(tm)

with printer_lock:
    print 'Critical section 1'
    print 'Critical section 2'

# Build context manager ################################

class CM(object):

    def __init__(self, x):
        self.x = x
        print 'Initialized with', x

    def __enter__(self):
        print 'Entering CM and returning 42'
        return 42

    def __exit__(self, exctype, excinst, exctb):
        print 'Exiting the CM'
        print 'Exctype:', exctype
        if issubclass(exctype, KeyError):
            print 'Caught a Key Error'
            print 'The args are', excinst.args
            print 'Working as handled'
            return True
        print 'Returning None which is False'

## Normal Path ###

with CM(100) as y:
    print 'In the body with y:', y
    print 'In the middle'
    raise KeyError('bill')
    print 'At the end'
print 'Finishing up'
print '=' * 20

## Unhandled
try:
    with CM(100) as y:
        print 'In the body with y:', y
        print 'In the middle'
        raise IndexError('bill')
        print 'At the end'
    print 'Never get here either'
except IndexError:
    print 'Caught the index errow'
print 'Finishing up'
print '=' * 20


