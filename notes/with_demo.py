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

## How to make a context manager ################

class CM(object):

    def __init__(self, x):
        self.x = x
        print 'Initializing with', x

    def __enter__(self):
        print 'Entering the CM and returning 42'
        return 42

    def __exit__(self, exctype, excinst, exctb):
        print 'Exiting the CM'
        print 'Exctype:', exctype
        if isinstance(excinst, KeyError):
            print 'Caught a KeyError'
            print 'The args are:', excinst.args
            print 'Marking as handled'
            return True
        print 'Returning None which is False'

## Normal path ##################################

print 'Starting up'
with CM(100) as y:
    print 'In the body with y:', y
    print 'In the middle'
    print 'At the end'
print 'Finishing up'
print '=' * 20

## Handled exception path ########################

print 'Starting up'
with CM(100) as y:
    print 'In the body with y:', y
    print 'In the middle'
    raise KeyError('bill')
    print 'Never get here'
print 'Finishing up'
print '=' * 20
        
## Unhandled exception path ######################

print 'Starting up'
try:
    with CM(100) as y:
        print 'In the body with y:', y
        print 'In the middle'
        raise IndexError(10)
        print 'Never get here'
    print 'Never get here either'
except IndexError:
    print 'Caught the IndexError'
print 'Finishing up'
print '=' * 20

## How Files Work in Python ######################

class File:

    def __init__(self, filename, mode='r', flags=0466):
        self.filename = filename
        self.mode = mode
        imode = {'r': ros.O_CREAT, 'w': ros.O_APPEND}
        fd = ros.creat(filename, imode)
        self.fd = fd
        self.status = 'open'

    def read(self, n=None):
        if self.status == 'closed':
            raise ValueError('I/O operation on closed file')
        n = n or -1
        return ros.read(self.fd, n)

    def close(self):
        ros.close(self.fd)
        self.status = 'closed'
    
    def __repr__(self):
         return '<%s file %r, mode %r at 0x%08x>' % (
             self.filename, self.mode, id(self))

    def __enter__(self):
        return self

    def __exit__(self, exctype, excinst, exctb):
        self.close()

def open(filename, mode='r', flags=0466):
    return File(filename, mode='r', flags=0466):

## How Locks Work in Python ######################

class Lock:

    def __init__(self):
        self.ld = ros.mlock()
        self.status = 'unlocked'

    def acquire(self):
        ros.aquir(self.ld)
        self.status = 'locked'

    def release(self):
        ros.releas(self.ld)
        self.status = 'unlocked'

    def __enter__(self):
        self.acquire()
        return self

    def __exit__(self, exctype, excinst, exctb):
        self.release()

