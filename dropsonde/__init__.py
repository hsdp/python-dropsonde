from .__version__ import __version__
import re
import traceback
import importlib
import pkgutil
import six
import sys


def list_modules(package):
    for importer, modname, ispkg in pkgutil.iter_modules(package.__path__):
        try:
            yield importlib.import_module('.' + modname, package.__name__)
        except Exception:
            traceback.print_exc()
            raise


try:
    if six.PY3:
        from . import py3 as pb
    else:
        from . import py2 as pb

    _self = sys.modules[__name__]
    for mod in list_modules(pb):
        name = mod.__name__.split('.')[-1]
        setattr(_self, name, mod)
        if name.endswith('_pb2'):
            name = re.sub('_pb2$', '', name)
            setattr(_self, name, mod)
            setattr(pb, name, mod)

except Exception:
    traceback.print_exc()
    raise
