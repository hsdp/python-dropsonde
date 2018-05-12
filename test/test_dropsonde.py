import six
from unittest import TestCase


class Dropsonde(TestCase):
    def test_import(self):
        import dropsonde

    def test_import_submodules(self):
        import dropsonde
        from dropsonde import list_modules, pb
        for module in list_modules(pb):
            name = module.__name__.split('.')[-1]
            self.assertEqual(module, getattr(dropsonde, name))
            self.assertEqual(module, getattr(pb, name))

    def test_import_pb(self):
        from dropsonde import pb

    if six.PY3:
        def test_import_py3(self):
            from dropsonde import py3

    else:
        def test_import_py2(self):
            from dropsonde import py2
