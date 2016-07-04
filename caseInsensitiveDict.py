'''Goal:Learn to customize built-in types
   Also: See example of th Open Closed Principle built into the language
'''

class CIDict(dict):
    'Customize dict that does case insensitive loads and stores'

    def __setitem__(self, key, value):
        print '.'
        self.key = key.upper()
        dict.__setitem__(self, key.upper(), value)

    def __getitem__(self, key):
        return dict.__getitem__(self, key.upper())

price = CIDict()

price['toaster'] = 15.76
price['iron'] = 10.54

print price['Toaster']
print 
