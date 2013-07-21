from calc.calc_exception import NotImplementError

class base_calc(object):

    def __init__(self):
        super(base_calc, self).__init__()

    def add(self, num):
        raise NotImplementError

    def sub(self, num):
        raise NotImplementError

    def time(self, num):
        raise NotImplementError

    def div(self, num):
        raise NotImplementError

    def pow(self):
        raise NotImplementError

    def pown(self, n):
        raise NotImplementError

    @property
    def result(self):
        raise NotImplementError

