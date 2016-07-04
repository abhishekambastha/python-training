'Fancy, expensive math package for rich people who have forgotten everything since 7th grade'

import math

pi = 3.14157

def area(radius):
    '''Compute the area of a circle

        >>> area(10)
        314.15700000000004

    '''
    return pi * radius ** 2.0

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

def area_traingle(base, height):
    '''Return the area of triangle
       >>> area_traingle(1,2)
        1.0
    '''
    return 0.5 * base * height

if __name__ == '__main__':
    import doctest

    print doctest.testmod()
