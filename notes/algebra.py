'Fancy, expensive math package for rich people who have forgotten everything since 7th grade'
# Copyright (c) 2016 Fly by night Software
# All Rights Reserved

# This code has three bad flaws that we are going to fix later (without changing the code)

import math

pi = 3.14157

def area(radius):
    '''Compute the area of a circle

        >>> area(10)
        314.15700000000004

    '''
    return pi * radius ** 2.0

def area_triangle(base, height):
    '''Return the area of a triangle

        >>> area_triangle(base=10, height=6)
        30.0

    '''
    if base < 0.0 or height < 0.0:
        raise RuntimeError('Imaginary numbers are only supported in complex arithmetic')
    return 0.5 * base * height

def quadratic(a, b, c):
    ''' Return two root of the quadratic equation:  ax^2 + bx + c = 0

        >>> x1, x2 = quadratic(a=8, b=22, c=15)
        >>> 8 * x1**2.0 + 22 * x1 + 15
        0.0
        >>> 8 * x2**2.0 + 22 * x2 + 15
        0.0
        >>> x1, x2
        (-1.25, -1.5)

    '''
    discriminant = math.sqrt(b ** 2.0 - 4.0 * a * c)
    x1 = (-b + discriminant) / (2.0 * a)
    x2 = (-b - discriminant) / (2.0 * a)
    return x1, x2

if __name__ == '__main__':
    import doctest

    print doctest.testmod()

