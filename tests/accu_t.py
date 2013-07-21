import tests
from calc import calc_factory

calc_name = "accu"
class test_accu_add(tests.TestCase):
    """ test_accu_add
    """

    def setUp(self):
        self.calc = calc_factory(calc_name).calc()

    def runTest(self):
        self.assertEquals(self.calc.result, 0)

        self.calc.add(10)
        self.assertEquals(self.calc.result, 10)

        self.calc.add(-10)
        self.assertEquals(self.calc.result, 0)

class test_accu_add2(tests.TestCase):
    """ test_accu_add2
    """

    def setUp(self):
        self.calc = calc_factory(calc_name).calc(20)

    def runTest(self):
        self.assertEquals(self.calc.result, 20)

        self.calc.add(10)
        self.assertEquals(self.calc.result, 30)

        self.calc.add(-10)
        self.assertEquals(self.calc.result, 20)

class test_accu_sub(tests.TestCase):
    """ test_accu_sub
    """

    def setUp(self):
        self.calc = calc_factory(calc_name).calc(10)

    def runTest(self):
        self.assertEquals(self.calc.result, 10)

        self.calc.sub(10)
        self.assertEquals(self.calc.result, 0)

        self.calc.sub(10)
        self.assertEquals(self.calc.result, -10)

class test_accu_time(tests.TestCase):
    """ test_accu_time
    """

    def setUp(self):
        self.calc = calc_factory(calc_name).calc()

    def runTest(self):
        self.assertEquals(self.calc.result, 0)

        self.calc.time(10)
        self.assertEquals(self.calc.result, 0)

        self.calc.add(10)
        self.calc.time(10)
        self.assertEquals(self.calc.result, 100)

        self.calc.time(-10)
        self.assertEquals(self.calc.result, -1000)

class test_accu_div(tests.TestCase):
    """ test_accu_div
    """

    def setUp(self):
        self.calc = calc_factory(calc_name).calc()

    def runTest(self):
        self.assertEquals(self.calc.result, 0)

        self.calc.div(10)
        self.assertEquals(self.calc.result, 0)

        self.calc.add(10)
        self.calc.div(10)
        self.assertEquals(self.calc.result, 1)

        self.calc.div(10)
        self.assertEquals(self.calc.result, 0.1)

class test_accu_pow(tests.TestCase):
    """ test_accu_pow
    """

    def setUp(self):
        self.calc = calc_factory(calc_name).calc()

    def runTest(self):
        self.assertEquals(self.calc.result, 0)

        self.calc.pow()
        self.assertEquals(self.calc.result, 0)

        self.calc.add(10)
        self.calc.pow()
        self.assertEquals(self.calc.result, 100)

        self.calc.pow()
        self.assertEquals(self.calc.result, 10000)

class test_accu_pown(tests.TestCase):
    """ test_accu_pown
    """

    def setUp(self):
        self.calc = calc_factory(calc_name).calc()

    def runTest(self):
        self.assertEquals(self.calc.result, 0)

        self.calc.pown(100)
        self.assertEquals(self.calc.result, 0)

        self.calc.add(10)
        self.calc.pown(4)
        self.assertEquals(self.calc.result, 10000)

