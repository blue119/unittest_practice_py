import tests
from calc import calc_factory
from calc.calc_exception import NotImplementError

class test_factory(tests.TestCase):
    """ test_factory
    """
    def setUp(self):
        self.calc = calc_factory().calc()

    def runTest(self):
        try:
            raise NotImplementError, 'unittest OK!!'
        except NotImplementError, e:
            self.assertEqual(str(e), "Not Implement: unittest OK!!")


