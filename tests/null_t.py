import tests
from calc import calc_factory
from calc.calc_exception import NotImplementError

calc_name = "null"
class test_null_result(tests.TestCase):
    """ test_null_add
    """

    def setUp(self):
        self.calc = calc_factory(calc_name).calc()

    def runTest(self):
        with self.assertRaises(NotImplementError):
            self.calc.result

class test_null_add(tests.TestCase):
    """ test_null_add
    """

    def setUp(self):
        self.calc = calc_factory(calc_name).calc()

    def runTest(self):
        with self.assertRaises(NotImplementError):
            self.calc.add(2)

class test_null_sub(tests.TestCase):
    """ test_null_sub
    """

    def setUp(self):
        self.calc = calc_factory(calc_name).calc(10)

    def runTest(self):
        with self.assertRaises(NotImplementError):
            self.calc.sub(3)

class test_null_time(tests.TestCase):
    """ test_null_time
    """

    def setUp(self):
        self.calc = calc_factory(calc_name).calc()

    def runTest(self):
        with self.assertRaises(NotImplementError):
            self.calc.time(2)

class test_null_div(tests.TestCase):
    """ test_null_div
    """

    def setUp(self):
        self.calc = calc_factory(calc_name).calc()

    def runTest(self):
        with self.assertRaises(NotImplementError):
            self.calc.div(2)

class test_null_pow(tests.TestCase):
    """ test_null_pow
    """

    def setUp(self):
        self.calc = calc_factory(calc_name).calc()

    def runTest(self):
        with self.assertRaises(NotImplementError):
            self.calc.pow()

class test_null_pown(tests.TestCase):
    """ test_null_pown
    """

    def setUp(self):
        self.calc = calc_factory(calc_name).calc()

    def runTest(self):
        with self.assertRaises(NotImplementError):
            self.calc.pown(2)


