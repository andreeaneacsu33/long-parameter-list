from data.data_extraction import Extractor
from data.data_processing import Processor


def run_test():
    print('Extracting data...')
    ext = Extractor('C:\\Users\\andre\\PycharmProjects\\django\\django')
    methods = ext.extract_methods()
    proc = Processor(methods)
    proc.process_data()
    methods = proc.get_methods()
    for method in methods:
        print(method)

    p_frequency = proc.get_parameters_frequency()
    print(p_frequency)


run_test()
