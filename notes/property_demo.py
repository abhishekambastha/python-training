'''Become a black belt with properties

Fundamental action:  Converts attribute access
    like p.midpoint into method access like p.midpoint()

Mechanism (how it works):  Reprograms the dot which can only
    be done in new-style classes that inherit from object.

Computed fields using properties:

    * Save storage space
    * Reduce risk of data inconsistency
    * Provide a clean, consistent API

Managed attributes:

    * Control ALL read and write access to a variable
    * A primary use case is validating data at the time the variable is written
    * This is a fantastic way to track down data corruption bugs which are
      otherwise notoriously hard to locate (like crickets in a dark room).

It is common to have a separate module of data validators:

    * validate_percentage
    * validate_str(minsize=3, maxsize=5, predicate=str.isupper)
    * validate_between(low=500, high=100)
    * valiaate_is_url

'''

from __future__ import division
from validators import validate_percentage

class PriceRange(object):
    'Store the daily price for a security'

    def __init__(self, symbol, low, high):
        self.symbol = symbol
        self.low = low
        self.high = high

    @property                                       # midpoint = property(midpoint)
    def midpoint(self):
        return (self.low + self.high) / 2

    # Managed attribute ##################

    @property
    def low(self):
        return self._low

    @low.setter
    def low(self, low):
        validate_percentage(low)
        self._low = low

    @property
    def high(self):
        return self._high

    @high.setter
    def high(self, high):
        validate_percentage(high)
        self._high = high

    def __repr__(self):
        return 'PriceRange(%r, %r, %r)' % (self.symbol, self.low, self.high)

p = PriceRange('CSCO', 20, 29)
