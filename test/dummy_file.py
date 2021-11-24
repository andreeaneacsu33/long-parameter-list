def dummy_method_a(param1, param2, param3, param4):
    pass


def dummy_method_b(self, param2, param3):
    pass


def dummy_method_c(param1, param2, param3, param4='value'):
    pass


def dummy_method_d(param1, param2, param3, param4, param5):
    pass


class Main:

    def __init__(self):
        self.a = 1

    def class_method(self):
        dummy_method_c(1, 2, 3, 'a')
        self.a = 2
