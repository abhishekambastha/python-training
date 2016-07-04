''' Compute the world famous Fibonacci function

    See: https://en.wikipedia.org/wiki/Dynamic_programming
    See: https://en.wikipedia.org/wiki/Fibonacci_number

        F(0)    ->  0
        F(1)    ->  1
        F(n)    ->  F(n-1) + F(n-2)  where n >= 2

'''

from decorator_school import cache

def fibo(n):
    a, b = 0, 1
    for i in xrange(n):
        a, b = b, a+b
    return a

@cache
def fibo(n):
    if n == 0: return 0
    if n == 1: return 1
    return fibo(n-1) + fibo(n-2)

if __name__ == '__main__':

    print fibo(200)
