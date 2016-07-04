''' Circuitous(tm)                               # Name of company or project
An advanced circle analytics company             # Elevator Pitch <--> Mission Statement
'''

# The sole the purpose of inheritance is code re-use
# New-style classes inherit from object that has __getattribute__ with a reprogrammable dot
# We tend to document before we write code:  it is easy, it focuses the mind
# "self" is a Python convention for the instance variable
# When copying from one namespace to another, we typically keep the name the same
# We don't tend to abbreviate in Python because of international audience
# and because we lack type declarations.
# We don't tend to put docstrings in dunder methods because 1) users don't see them
# and 2) because they have a standard meaning.
# D.R.Y. Principle == Do Not Repeat Yourself == There should be a single source of truth
# Code Smell == Code that works but has understandability or maintenance issues
# The purpose of modules is 1) to organize code and 2) as a principal tool for code reuse
# Give "magic constants" a name and constants should have upper case letters in the name
# "Code is your enemy" in particular, it is the enemy of agility.
# "Clash" to with core problem directly and aggressively
# MVP --> Minimum viable product is the smallest real solution to a real problem
# YAGNI,RN --> You ain't gonna need it, right now.
# Dogfooding --> Be the first user of your product
# After dogfooding -> Beta testing (external users)
# Technical Debt --> Temporarily avoiding refactoring in order to meet deadline
# the key is to have made plans to pay down the debt rather than letting it accumulate


import math
from collections import namedtuple      # named tuples make code more self-documenting

Version = namedtuple('Version', ['major', 'minor', 'micro'])

class Circle(object):
    'An advanced circle analytic toolkit'
    __slot__ = ['diameter']             #Implement the Flyweight Design Pattern

    version = Version(0, 20, 1)          # class attributes are shared by all instances

    def __init__(self, radius):
        self.radius = radius            # instance variables have data unique to each instance

    def area(self):
        'Perform quadrature on a planar shape of uniform revolution'
        p = self.perimeter()
        radius = p / 2.0 / math.pi
        return math.pi * self.radius ** 2.0

    def perimeter(self):
        'Compute the closed line integral of the 2-D locus of points equidistant from a given point'
        return 2.0 * math.pi * self.radius

    # Best practice for __repr__ is to look like how the object could have been creeated
    def __repr__(self):
        return 'Circle(%r)' % self.radius

    @staticmethod
    def angle_to_grade(angle):
        'Convert an inclinometer reading in degrees to a percent grade'
        return math.tan(math.radians(angle)) * 100

    #angle_to_grade = staticmethod(angle_to_grade)

    @classmethod
    def from_bbd(cls, bbd):
        'Create a new cirle form bounding box'
        radius = bbd / 2.0 / math.sqrt(2)
        return cls(radius)

    #from_bbd = classmethod(from_bbd)

    @property
    def radius(self):
        return self.diameter / 2.0

    @radius.setter
    def radius(self, radius):
        self.diameter = radius * 2.0

    #radius = property(get_radius, set_radius)
    # property reprogrammes the dot

