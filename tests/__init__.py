# -*- coding: utf-8 -*-

import os
import sys
import tempfile
import tempfile
import types
import glob
import unittest

# This list also determines the order in which tests will executed
__all__ = []
for file in glob.glob(os.path.dirname(__file__) + '/*.py'):
    name = os.path.basename(file)[:-3]
    if name[-2:] == '_t': __all__.append(name)

def all_files():
    """docstring for all calc's files"""
    files = []
    for file in glob.glob('calc/*.py'):
        if file[-3:] == '.py': files.append(file)
    return files

def load_tests(loader, tests, pattern):
    '''Load all test cases and return a unittest.TestSuite object.
    The parameters 'tests' and 'pattern' are ignored.
    '''
    print 'load_tests'
    suite = unittest.TestSuite()
    for name in ['tests.'+name for name in __all__ ]:
        test = loader.loadTestsFromName(name)
        suite.addTest(test)
    return suite

class TestCase(unittest.TestCase):
    '''Base class for test cases'''

    def assertEqual(self, first, second, msg=None):
        ## HACK to work around bug in unittest - it does not consider
        ## string and unicode to be of the same type and thus does not
        ## show diffs
        ## TODO file bug report for this
        if type(first) in (str, unicode) \
        and type(second) in (str, unicode):
            self.assertMultiLineEqual(second, first, msg)
            ## HACK switch arguments here, otherwise order of
            ## diff is wrong (assuming first is what we got and second
            ## is the reference)
        else:
            unittest.TestCase.assertEqual(self, first, second, msg)

