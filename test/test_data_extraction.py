from data.data_extraction import Extractor


def run_test():
    print('Extracting data...')
    ext = Extractor('.')
    methods = ext.extract_methods()
    for method in methods:
        print(method)


run_test()
