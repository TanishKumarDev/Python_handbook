# OrderedDict is a subclass of Python's built-in dictionary dict that remembers the order in which keys are inserted. Unlike older versions of Python where dictionaries did not guarantee order, OrderedDict preserves insertion order reliably.
from collections import OrderedDict

od = OrderedDict()
od['apple'] = 1
od['banana'] = 2
od['cherry'] = 3
print(od)


