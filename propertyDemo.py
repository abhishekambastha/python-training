'Become a black belt in property'
'property can be used by inheriting object for a reprogrammable dot'

from validater import validate_percentage

class PriceRange(object):
    'Store the daily price for a security'

    def __init__(self, low, high):
        self.symbol = symbol
        self.low = low
        self.high = high
        #self.midpoint = (low + high) / 2.0 #Not good, data inconsistancy

    @property
    def midpoint():
        return (self.low + self.high) / 2.0

    #midpoint = property(midpoint)

    def __repr__(self):
        return "PriceRange('%r %r %r')" % (self.symbol, self.low, self.high)

    # Managed attribute ###########################################
    @property
    def low(self):
        return self._low

    @low.setter
    def low(self, low):
       self._low = low

    #low = property(get_low, set_low)


    @property
    def high(self):
        return self._high

    @high.setter
    def high(self, high):
        self._high = high
