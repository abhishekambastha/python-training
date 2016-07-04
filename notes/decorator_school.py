from functools import wraps

def add_logging(origfunc):
    @wraps(origfunc)
    def logging_func(x):
        print '%s() was called with %r' % (origfunc.__name__, x)
        answer = origfunc(x)
        print 'the answer is', x
        return answer
    return logging_func

def cache(orig_func):
    answers = {}
    @wraps(orig_func)
    def inner(x):
        if x in answers:
            return answers[x]
        answer = orig_func(x)
        answers[x] = answer
        return answer
    return inner

dispatch = {}                             # external_func_name : internal_func_implementation

def interpret(x):
    ''' Build a simple interactive programming language

        >>> interpret(10)
        Enter a program: co sq co co cu
        10 --(co)--> 5 --(sq)--> 25 --(co)--> 76 --(co)--> 38 --(cu)--> 54872

        >>> interpret(5)
        Enter a program: sq co co cu
        5 --(sq)--> 25 --(co)--> 76 --(co)--> 38 --(cu)--> 54872

    '''
    program = raw_input('Enter a program: ')
    print x,
    for command in program.split():
        x = dispatch[command](x)
        print '--(%s)--> %s' % (command, x),
    print

def register(external):
    'A higher-order non-pure identity function for registering external names to functions'
    def deco(func):
        dispatch[external] = func
        return func
    return deco


#################################################################################

if __name__ == '__main__':
    import time

    @add_logging                           # square = add_logging(square)
    @register('sq')                        # dispatch['sq'] = square
    def square(x):
        return x * x

    @cache
    @add_logging
    @register('cu')
    def cube(x):
        'Return a value times itself thrice'
        return x ** 3

    @register('co')
    def collatz(x):
        return x // 2 if x % 2 == 0 else 3 * x + 1

    @register('ha')
    def half(x):
        return x // 3

    @cache
    def big_calc(x):
        'Simulate a slow computational intensive function or a func that has I/O blocking'
        print 'Doing hard work!'
        time.sleep(1)
        return x + 1

    y = square(5)
    z = cube(11)
    print big_calc(10)
    print big_calc(20)
    print big_calc(10)

    ##bc_answers = {}               # question -> answer
    ##
    ##def big_calc(x):
    ##    'Simulate a slow computational intensive function or a func that has I/O blocking'
    ##    if x in bc_answers:
    ##        return bc_answers[x]
    ##    print 'Doing hard work!'
    ##    time.sleep(1)
    ##    answer = x + 1
    ##    bc_answers[x] = answer
    ##    return answer
    ##
    ##cu_answers = {}
    ##
    ##def cube(x):
    ##    if x in cu_answers:
    ##        return cu_answers[x]
    ##    answer = x ** 3
    ##    cu_answers[x] = answer
    ##    return answer
