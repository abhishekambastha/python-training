from pprint import pprint
from collections import OrderedDict

resp = [
    {'id': 1804, 'status': 'up', 'location': 'sj'},
    {'id': 1802, 'status': 'down', 'location': 'la'},
    {'id': 1801, 'status': 'up', 'location': 'nv'},
    {'id': 1805, 'status': 'down', 'location': 'tx'},
]

# How to order the list of dicts ###################

pprint(sorted(resp, key=lambda d: d['id']))

# How to order the dicts themselves ################

for i, rd in enumerate(resp):
    resp[i] = OrderedDict(sorted(rd.items()))

pprint(resp)

# How to compare to a reference dict ###############

ref = {'id': 1800, 'status': 'down', 'location': 'sj'}
print sorted(set(resp[0].items()) - set(ref.items()))
print sorted(resp[0].viewitems() - ref.viewitems())
