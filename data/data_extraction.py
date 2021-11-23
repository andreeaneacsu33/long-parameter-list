import os
import re


class Method(object):
    description = "Class for the method representation"

    def __init__(self, name, parameter_list):
        self._name = name
        self._parameter_list = parameter_list

    def get_name(self):
        return self._name

    def get_parameter_list(self):
        return self._parameter_list

    def __str__(self):
        return '{} {}'.format(self._name, self._parameter_list)


class Extractor(object):
    description = "Class for extracting methods from source code files"
    EXCLUDED_PARAMETERS = ['self', 'cls']
    EXCLUDED_CHARACTER = "="

    def __init__(self, directory):
        self._directory = directory

    def extract_methods(self):
        methods = []
        for root, dirs, files in os.walk(self._directory):
            for file in files:
                file_path = root + '/' + file
                file_methods = self._extract_file_methods(file_path)
                methods = methods + file_methods
        return methods

    def _extract_file_methods(self, filename):
        """
        Method that reads a file and extracts all the methods' name and parameters
        :param filename: name of the file
        :return: the list of methods
        """
        methods = []
        f = open(filename, 'r')
        methods_signature = self._get_methods_signature(f)

        for name, parameters in methods_signature:
            parameters = self._filter_parameters(parameters)
            method = Method(name, parameters if parameters else [])
            methods.append(method)
        return methods

    def _filter_parameters(self, parameters):
        """
        Method that excludes from the list the default parameters
        and the class related ones
        :param parameters: list of parameters
        :return: the modified list of parameters
        """
        parameters_list = parameters.replace(' ', '').split(',')
        return [parameter for parameter in parameters_list
                if parameter not in self.EXCLUDED_PARAMETERS
                and self.EXCLUDED_CHARACTER not in parameter]

    @staticmethod
    def _get_methods_signature(f):
        pattern = r"def ([a-z_]+)\s*\((.*?)\):"
        return re.findall(pattern, f.read())
