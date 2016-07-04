# XXX -- Top level review comments:
#
# * Nice exception recovery and logging.
#
# * Please cleanup code formatting.
#   This is a little rough on my eyes.
#
# * Should we use this as template for other
#   short network element scripts?
#
# -- Thanks.   The Boss :-)

import jnettool.tools.elements.NetworkElement
import jnettool.tools.Routing
import jnettool.tools.RouteInspector

ne = jnettool.tools.elements.NetworkElement('171.0.2.45')

try:
    routing_table = ne.getRoutingTable()

except jnettool.tools.elements.MissingVar:
    logging.exception('No routing table found')
    ne.cleanup('rollback')

else:
    num_routes = routing_table.getSize()
    for i in range(num_routes):
        route = routing_table.getRouteByIndex(i)
        name = route.getName()
        ipaddr = route.getIPAddr()
        print '%15s -> %s' % (ipaddr, name)
    ne.cleanup('commit')

finally:
    ne.disconnect()











