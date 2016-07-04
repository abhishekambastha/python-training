import threading

f = open('notes/hamlet.txt')
try:
    play = f.read()
    print len(play)
finally:
    f.close()

with open('notes/hamlet.txt') as f:
    play = f.read()
    print len(play)
# How to make locks

printer_lock = threading.Lock()

printer_lock.acquire()
try:
    print 'Critical sec1'
    print 'Critical sec2'
finally:
    printer_lock.release()


with printer_lock:
    print 'Critical sec1'
    print 'Critical sec2'

