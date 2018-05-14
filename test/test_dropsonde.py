import sys
import six
import pkgutil
import importlib
from unittest import TestCase


def load_modules(package):
    for importer, modname, ispkg in pkgutil.iter_modules(package.__path__):
        yield importlib.import_module('.' + modname, package.__name__)


class Dropsonde(TestCase):
    def test_import(self):
        import dropsonde

    def test_import_submodules(self):
        from dropsonde import pb
        for module in load_modules(pb): pass

    def test_import_pb(self):
        from dropsonde import pb
