import warnings
import math

def Asqrt(x):
    if x > 0.0:
        return math.sqrt(x)
    else:
        warnings.warn('Caution!, taking square root of -ve number')
        return math.sqrt((-1)*x) * 1j

def user(x):
    return Asqrt(x**3)

warnings.filterwarnings('ignore', ".*square root*")
print user(5)
print user(-5)

