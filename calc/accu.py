from calc.base import base_calc

class calc(base_calc):

    def __init__(self, num = 0):
        super(calc, self).__init__()
        self.__result = float(num)

    def add(self, num):
        self.__result += num
        return self

    def sub(self, num):
        self.__result -= num
        return self

    def time(self, num):
        self.__result *= num
        return self

    def div(self, num):
        self.__result /= num
        return self

    def pow(self):
        self.__result *= self.__result
        return self

    def pown(self, n):
        oldValue = self.__result
        for i in xrange(n-1):
            self.__result *= oldValue
        return self

    @property
    def result(self):
        return self.__result

