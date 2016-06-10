import inspect
import sys
from ideax.settings import base


_names = set([])


for name, value in inspect.getmembers(base):
    if not name.startswith('__'):
        _names.add(name)
        setattr(sys.modules[__name__], name, value)


try:
    from ideax.settings import local
    for name, value in inspect.getmembers(local):
        if name in _names:
            setattr(sys.modules[__name__], name, value)
        elif not name.startswith('__'):
            print ('Could not load local setting %s as '
                   'there is no base setting to override.') % name
except ImportError, e:
    raise ImportError("Failed to import local settings")
