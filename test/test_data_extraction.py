from data.data_extraction import Extractor
from data.data_processing import Processor


def run_test():
    print('Extracting data...')
    ext = Extractor('.')
    methods = ext.extract_methods()
    proc = Processor(methods)
    methods = proc.process_data()
    for method in methods:
        print(method)


run_test()
