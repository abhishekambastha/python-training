import warnings
import math

# Concept Map
# ----------------------------------------------------------------------------------------------
# Policies are called "actions":  error, ignore, always, default (1st only from each play), once
# "Messages" are the text that goes with the warning
# "Category" an exception class:  UserWarning, DeprecationWarnings, SyntaxWarning, RuntimeWarning, ImportWarning, UnicodeWarning
# "Module" is where the warning is created
# "Line number"

def sqrt(x):
    if x >= 0.0:
        return math.sqrt(x)
    warnings.warn('Caution, taking a square root of a negative number')
    return math.sqrt(-x) * 1j

def user(x):
    return sqrt(x ** 3)

warnings.filterwarnings("always", ".*square root.*")
#                         ^-- action   ^-- regex on the message

#warnings.filterwarnings("error", category=UserWarning)
#                         ^-- action   ^-- match the category

print user(5)
print user(-5)
print user(6)
print user(-6)
