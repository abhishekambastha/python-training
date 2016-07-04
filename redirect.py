'Goals:  Learn patterns output directions and motivate practical context managers'

import sys
from StringIO import StringIO
from dis import dis

class Redirect(object):
    def __init__(self, target):
        self.target = target

    def __enter__(self):
        self.oldstdout = sys.stdout

    def __exit__(self, extype, exinst, extb):

def show_family(lastname, first_names):
    'Display family members in a nice tabular format'
    print 'The %s Family' % lastname.title()
    print '=' * (11 + len(lastname))
    for name in first_names:
        print '* %s' % name.title()
    print


f = StringIO()
try:
    oldstdout = sys.stdout
    sys.stdout = f
    try:
        show_family('simpsons', ['homer', 'marge', 'bart', 'lisa', 'maggie'])
    finally:
        sys.stdout = oldstdout
    s = f.getvalue()
    print s.upper()
finally:
    f.close()

f = open('show_family_dis.txt', 'w')
try:
    oldstdout = sys.stdout
    sys.stdout = f
    try:
        dis(show_family)
    finally:
        sys.stdout = oldstdout
finally:
    f.close()

oldstdout = sys.stdout
sys.stdout = sys.stderr
try:
    help(show_family)
finally:
    sys.stdout = oldstdout

print 'Done!'
print '=' * 20
