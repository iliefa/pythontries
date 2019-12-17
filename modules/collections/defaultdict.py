#works like a dict, it's initialized with a function("default factory")
#provides the default value for a nonexistent key
#will never raise KeyError

from collections import defaultdict

ice_cream = defaultdict(lambda: 'Vanilla')
ice_cream['sarah']='top gun'
ice_cream['john'] = 'joe'
print(ice_cream['andrew'])