''' Adaptor Pattern
Intermdiate python
'''


import jnettool.tools.elements.NetworkElement
import jnettool.tools.Routing
import jnettool.tools.RouteInspector

class NetworkElement(object):

    def __init__(self, ipaddr):
        self.ipaddr = ipaddr
        self.oldelem = jnettool.tools.element.NetworkElement

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.ipaddr)

    def __enter__(self):
        return self

    def __exit__(self, extype, exinst, exctb):
        if extype = jnettool.tools.elements.MissingVar:
            logging.exception('No routing table found')
            self.oldelem.cleanup('rollback')

    @property
    def routing_table(self):
        return RoutingTable(self.oldelem.getRoutingTable())

class RoutingTable(object):

    def __init__(self, oldroutetable):
        self.oldroutetable = oldroutetable

    def __len__(self):
        return self.oldroutetable.getSize()

    def __getitem__(self, index):
        if index >= len(self):
            raise IndexError('Route number out of range')
        return self.oldroutetable.getRouteByIndex(index)

class Route(object):

    def __init__(self, oldroute):
        self.oldroute = oldroute

    @property
    def name(self):
        return self.oldroute.getName()

    @property
    def ipaddr(self):
        return self.oldroute.getIPAddr()
