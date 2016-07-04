'''
Monkey patching is making variable

When monkey patching occurs, something bad is happening

'''

import algebra
import math

algebra.pi = math.pi

orig_area_triangle = algebra.area_traingle  #save ref

def better_area_traingle(*args, **kwargs):  #make wrapper
    try:
        return orig_area_triangle(*args, **kwargs)
    except RuntimeError:
        raise ValueError('Unusable arguments (check)')

algebra.area_traingle = better_area_traingle #Monkey patching

orig_sqrt = math.sqrt

def better_sqrt(x):
    'Support both posiitve and negative inputs'
    if x >= 0.0:
        return sqrt(x)
    else:
        return -1j * orig_sqrt(x * (-1))

math.sqrt = better_sqrt

print algebra.area_traingle(20, 15)
print algebra.area_traingle(20, -15)
