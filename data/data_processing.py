
class Processor:
    description = "Class for processing the extracted data"
    METHOD_PARAMETERS_LIMIT = 3

    def __init__(self, methods):
        self._methods = methods
        self._unique_parameters = []
        self._parameters_frequency = []

    def process_data(self):
        """
        Method that creates a set of unique parameters from
        the extracted methods that have more than a given limit of
        parameters
        """
        parameters = []
        parameters_lists = []
        self._methods = [method for method in self._methods
                         if len(method.get_parameter_list()) > self.METHOD_PARAMETERS_LIMIT]

        for method in self._methods:
            method_parameters = method.get_parameter_list()
            parameters_lists.append(method_parameters)
            parameters = parameters + method_parameters

        self._unique_parameters = set(parameters)
        self._create_parameters_frequency(parameters_lists, self._unique_parameters)

    def _create_parameters_frequency(self, parameters_lists, unique_parameters):
        parameters_frequency = []
        for p_list in parameters_lists:
            row = []
            for parameter in unique_parameters:
                if parameter in p_list:
                    row.append(1)
                else:
                    row.append(0)
            parameters_frequency.append(row)
        self._parameters_frequency = parameters_frequency
        print(unique_parameters)

    def get_methods(self):
        return self._methods

    def get_unique_parameters(self):
        return self._unique_parameters

    def get_parameters_frequency(self):
        return self._parameters_frequency


