''' Teach how mixins work, what inheritance is really about,
    how to use multiple inheritance, and how to use
    ABCs (abstract base classes) to impose discipline
    on mixins.

    This is all about code re-use!

'''

from abc import ABCMeta, abstractmethod

class Capper:

    __metaclass__ = ABCMeta                    # <== Inspector

    @abstractmethod                            # <== Specification for the 1st floor
    def __getitem__(self, index):
        raise IndexError

    def capitalize(self):                      # <== 2nd floor mixin capability
        return ''.join(self).upper()

class Uncapper:
    'Mixin class'

    def uncapitalize(self):
        return ''.join(self).lower()

################################################

from collections import Sequence

class DoubleSeq(Capper, Uncapper, Sequence):

    def __init__(self, seq):
        self.seq = seq

    def __len__(self):
        return (len(self.seq) + 1) // 2

    def __getitem__(self, index):
        if index >= len(self):
            raise IndexError('Index out of range')
        return self.seq[index * 2]

class TripleSeq(Capper, Uncapper, Sequence):

    def __init__(self, seq):
        self.seq = seq

    def __len__(self):
        return (len(self.seq) + 2) // 3

    def __getitem__(self, index):
        if index >= len(self):
            raise IndexError('Index out of range')
        return self.seq[index * 3]

if __name__ == '__main__':
    d = DoubleSeq("Hettinger")
    print len(d)
    print d[0], d[1], d[2]
    print d.capitalize()

    t = TripleSeq('Cisco Rocks and have embraced Python')
    print len(t)
    print list(t)
    print t.capitalize()

