import os

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt
from apyori import apriori

from data.data_extraction import Extractor
from data.data_processing import Processor


def main():
    ext = Extractor(os.environ.get('DIRECTORY_PATH'))
    methods = ext.extract_methods()
    proc = Processor(methods)
    proc.process_data()
    # methods = proc.get_methods()
    # for method in methods:
    #     print(method)

    p_frequency = proc.get_parameters_frequency()
    p_unique = proc.get_unique_parameters()

    parameters = pd.DataFrame(p_frequency, columns=p_unique)
    parameters.head()

    # parameter_support_dict = {}
    # for column in parameters.columns:
    #     parameter_support_dict[column] = sum(parameters[column] > 0)
    #
    # ts = pd.Series(parameter_support_dict)
    # ts.plot(kind="bar")
    # plt.show()

    association_rules = apriori(parameters, min_support=0.2)
    association_result = list(association_rules)
    print(len(association_result))
    for rule in association_result:
        print(rule)


if __name__ == "__main__":
    main()
