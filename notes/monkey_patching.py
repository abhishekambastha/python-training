''' Monkey patching is making variable assignments into other people's namespaces.

When monkey patching occurs, something BAD is happening.
The bad thing is the patchee's fault, not the patchor.

Legitimate use cases for monkey patching:
    * Fix an erroneous constant
    * Replace a external root url with mock server to testing purposes
    * Improve error message
    * Make more robusts -- handle a broader range on inputs
    * Add tracing and debugging to production code

'''

import algebra
import math

orig_area_triangle = algebra.area_triangle              # Step 1:  Save reference to original function

def better_area_triangle(*args, **kwds):                # Step 2:  Build a wrapper function
    'Wrap the area_triangle() to improve its error messages'
    try:
        return orig_area_triangle(*args, **kwds)
    except RuntimeError:
        raise ValueError('Unusable arguments (check to make sure the inputs are non-negative)')

algebra.area_triangle = better_area_triangle            # Step 3:  Monkey patch

algebra.pi = math.pi                                    # Constants can be monkey patched directly

orig_sqrt = math.sqrt                                   # Step 1:  Save reference to original function

def better_sqrt(x):                                     # Step 2:  Build a wrapper function
    'Support both positive and negative inputs to math.sqrt'
    if x >= 0.0:
        return orig_sqrt(x)
    return orig_sqrt(-x) * 1j

math.sqrt = better_sqrt                                 # Step 3:  Monkey patch

if __name__ == '__main__':
    try:
        print algebra.area_triangle(20, 15)
        print algebra.area_triangle(20, -15)
    except ValueError:
        print 'Oops, sorry about the negative number'

    print algebra.area(30)

    print algebra.quadratic(a=12, b=23, c=10)
    print algebra.quadratic(a=12, b=8, c=10)
