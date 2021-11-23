

class Method(object):

    def __init__(self, name, parameter_list):
        self.name = name
        self.parameter_list = parameter_list

    def get_name(self):
        return self.name

    def get_parameter_list(self):
        return self.parameter_list

