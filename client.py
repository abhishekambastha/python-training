"Show circuitous from the user's point of view"

from __future__ import division
from circuitous import Circle, angle_to_grade

print u'Tutorial for Circuitous\N{trade mark sign}'
print 'Software version %d.%d' % Circle.version[:2]
c = Circle(10)
print 'A circle with a radius of', c.radius
print 'has an area of', c.area()
print

## Academic Friends ##########################################################

from random import seed, random
from pprint import pprint

n = 10
jenny = 8675309

print 'DARPA grant proposal'
print 'to study the average area of random circles'
print 'using Circuitous version %d.%d' % Circle.version[:2]
print 'preliminary study using %d circles' % n
print "seeded using Jenny's number:", jenny
seed(jenny)
circles = [Circle(random()) for i in range(n)]
areas = [circle.area() for circle in circles]
average_area = sum(areas) / n
print 'The average area is %.1f' % average_area
print

## Rubber Sheet Company ######################################################

template = [0.1, 0.2, 0.7]
print 'Spec sheet for the template', template
circles = [Circle(cut_radius) for cut_radius in template]
for i, circle in enumerate(circles):
    print 'Circle #%d' % i
    print 'A rubber circle with a cut radius of', circle.radius
    print 'has a perimeter of', circle.perimeter()
    print 'and a cold area of', circle.area()
    circle.radius *= 1.1        # circle.set_radius(circle.get_radius() * 1.1)
    print 'and a warm area of', circle.area()
    print

## National Tire Chain #######################################################

class Tire(Circle):
    'Circle analytics with a perimeter for the rubber on the tire'

    RUBBER_RATIO = 1.25

    def perimeter(self):
        'Perimeter corrected for the rubber tire company'
        return Circle.perimeter(self) * self.RUBBER_RATIO

class MonsterTire(Tire):
    RUBBER_RATIO = 1.50

## National Trucking Company ##################################################


## National Graphic Company ###################################################

c = Circle.from_bbd(Circle, 25)
print 'A circle with a bounding box diameter with 25'
print 'has a radius of', c.radius
print 'an area of', c.area()
print 'and a perimeter of', c.perimeter()
