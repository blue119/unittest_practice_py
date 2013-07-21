import tests
from calc import calc_factory
from calc import accu, null, sci
from calc.calc_exception import NotImplementError

class test_factory(tests.TestCase):
    """ test_factory
    """

    def runTest(self):
        self.calc = calc_factory("null")
        self.assertEqual(self.calc, null)

        self.calc = calc_factory("nul")
        self.assertEqual(self.calc, null)

        self.calc = calc_factory("")
        self.assertEqual(self.calc, null)

        self.calc = calc_factory("accu")
        self.assertEqual(self.calc, accu)

        self.calc = calc_factory("sci")
        self.assertEqual(self.calc, sci)

