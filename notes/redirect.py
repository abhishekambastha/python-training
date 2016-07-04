'Goals:  Learn patterns output directions and motivate practical context managers'

import sys

class RedirectStdout(object):

    def __init__(self, target):
        self.target = target

    def __enter__(self):
        self.oldstdout = sys.stdout
        sys.stdout = self.target
        return self

    def __exit__(self, exctype, excinst, exctb):
        sys.stdout = self.oldstdout        

if __name__ == '__main__':

    from StringIO import StringIO
    from dis import dis
    from contextlib import closing

    def show_family(lastname, first_names):
        'Display family members in a nice tabular format'
        print 'The %s Family' % lastname.title()
        print '=' * (11 + len(lastname))
        for name in first_names:
            print '* %s' % name.title()
        print

    ######################## The New Awesome Way ##################################
        
    with closing(StringIO()) a f:
        with RedirectStdout(f):
            show_family('simpsons', ['homer', 'marge', 'bart', 'lisa', 'maggie'])
            s = f.getvalue()
        print s.upper()

    with open('show_family_dis.txt', 'w') as f:
        with RedirectStdout(f):
            dis(show_family)

    with RedirectStdout(sys.stderr):
        help(show_family)

    print 'Done!'
    print '=' * 20

    ########################## The Old Crummy Way ##################################
    ##    
    ##f = StringIO()
    ##try:
    ##    oldstdout = sys.stdout
    ##    sys.stdout = f
    ##    try:
    ##        show_family('simpsons', ['homer', 'marge', 'bart', 'lisa', 'maggie'])
    ##    finally:
    ##        sys.stdout = oldstdout
    ##    s = f.getvalue()
    ##    print s.upper()
    ##finally:
    ##    f.close()
    ##
    ##f = open('show_family_dis.txt', 'w')
    ##try:
    ##    oldstdout = sys.stdout
    ##    sys.stdout = f
    ##    try:
    ##        dis(show_family)
    ##    finally:
    ##        sys.stdout = oldstdout
    ##finally:
    ##    f.close()
    ##
    ##oldstdout = sys.stdout
    ##sys.stdout = sys.stderr
    ##try:
    ##    help(show_family)
    ##finally:
    ##    sys.stdout = oldstdout
    ##
    ##print 'Done!'
    ##print '=' * 20
