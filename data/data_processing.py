
class Processor:
    description = "Class for processing the extracted data"
    METHOD_PARAMETERS_LIMIT = 3

    def __init__(self, methods):
        self._methods = methods

    def process_data(self):
        return [method for method in self._methods
                if len(method.get_parameter_list()) > self.METHOD_PARAMETERS_LIMIT]



