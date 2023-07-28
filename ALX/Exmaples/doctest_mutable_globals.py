# doctest_mutable_globals.py

_module_data = {}


class TestGlobals:

    def one(self):
        """
        >>> TestGlobals().one()
        >>> 'var'in _module_data
        True
        """

    def two(self):
        """
        >>> 'var' in _module_data
        False
        """