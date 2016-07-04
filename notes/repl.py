'Goal:  Create a custom REPL for Python'

# https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop

In = []
Out = []

while True:
    expr = raw_input('In [%r]: ' % len(In))
    result = eval(expr)
    print 'Out[%r]: %r\n' % (len(Out), result)

    In.append(expr)
    Out.append(result)
