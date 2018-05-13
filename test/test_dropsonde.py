import six
import importlib
from unittest import TestCase


class Dropsonde(TestCase):
    def test_import(self):
        import dropsonde

    def test_import_submodules(self):
        import dropsonde
        from dropsonde import list_modules, get_last_name, pb
        for module in list_modules(pb):
            name = get_last_name(module)
            full_name = '.'.join([dropsonde.__name__, name])
            imported = importlib.import_module(full_name)
            self.assertEqual(module, getattr(dropsonde, name))
            self.assertEqual(module, getattr(pb, name))
            self.assertEqual(module, imported)

    def test_import_pb(self):
        from dropsonde import pb
