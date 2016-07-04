"Show circuitous from the user's point of view"

from __future__ import division
from circuitous import Circle

print u'Tutorial for Circuitous\N{trade mark sign}'
print 'Software version %d.%d' % Circle.version[:2]
c = Circle(10)
print 'A circle with a radius of', c.radius
print 'has an area of', c.area()
print

## Academic Friends ##########################################################

from random import seed, random
from pprint import pprint

n = 100000
jenny = 8675309

print 'DARPA grant proposal'
print 'to study the average area of random circles'
print 'using Circuitous version %d.%d' % Circle.version[:2]
print 'preliminary study using %d circles' % n
print "seeded using Jenny's number:", jenny
seed(jenny)
circles = [Circle(random()) for i in xrange(n)]
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
    'Circle analytics with a perimeter corrected for the rubber on the tire'

    RUBBER_RATIO = 1.25

    def perimeter(self):
        'Perimeter corrected for the rubber on the tire'
        return Circle.perimeter(self) * self.RUBBER_RATIO # Extending  The parent method is called and the results are modified
        # return 2.0 * 3.14 * self.radius * 1.25          # Overriding:  The parent method never gets called

    __perimeter = perimeter

class MonsterTire(Tire):
    'Circle analytics with a perimeter corrected for the rubber on the tire'

    RUBBER_RATIO = 1.50

t = Tire(30)
print 'A tire of radius %r inches' % t.radius
print 'has an inner cut-out area of', t.area()
print 'and a rubber corrected perimeter of', t.perimeter()
print

## National Trucking Company #################################################

print u'An inclinometer reading of 5\N{degree sign}',
print 'is a %.1f%% grade.' % Circle.angle_to_grade(5)
print

## National Graphics Company #################################################

c = Circle.from_bbd(25)
print 'A circle with a bounding box diagonalof 25'
print 'has a radius of', c.radius
print 'an area of', c.area()
print 'and a perimeter of', c.perimeter()
print

## US Gov't ##################################################################

# ISO 10666:  No circle software shall compute the area directly from a radius.
# It MUST first call perimeter and infer the radius or diameter indirectly.

# ISO 10667:  No circle software shall store the radius.  It MUST store the
# diameter and ONLY the diameter.



