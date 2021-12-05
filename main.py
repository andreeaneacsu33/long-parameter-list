import os

import pandas as pd
from efficient_apriori import apriori  # for association analysis

from data.data_extraction import Extractor
from data.data_processing import Processor


def _print_methods(proc):
    print('-- Extracted Methods --\n')
    methods = proc.get_methods()
    for method in methods:
        print(method)

def main():
    ext = Extractor(os.environ.get('DIRECTORY_PATH'))
    methods = ext.extract_methods()
    proc = Processor(methods)
    proc.process_data()

    # _print_methods(proc)

    p_frequency = proc.get_parameters_frequency()

    parameters_df = pd.DataFrame(p_frequency)

    # print(parameters_df.to_string())

    # Create a dataframe using this single list and add a column for count
    transactions = parameters_df.values.reshape(-1).tolist()

    parameters_df_list = pd.DataFrame(transactions)
    parameters_df_list['Count'] = 1

    # Group by items and rename columns
    parameters_df_list = parameters_df_list.groupby(by=[0], as_index=False).count().sort_values(by=['Count'], ascending=True)  # count
    parameters_df_list['Percentage'] = (parameters_df_list['Count'] / parameters_df_list['Count'].sum())  # percentage
    parameters_df_list = parameters_df_list.rename(columns={0: 'Item'})

    # print(parameters_df_list.to_string())

    # Prepare a list of lists to run apriori algorithm
    parameters_lists = parameters_df.stack().groupby(level=0).apply(list).tolist()

    # Show what it looks like
    for tx_list in parameters_lists:
        print(tx_list)

    itemsets, rules = apriori(parameters_lists, min_support=0.03, min_confidence=0.2, verbosity=1)
    print(itemsets)

    for item in sorted(rules, key=lambda item: (item.lift, item.conviction), reverse=True):
        print(item)


if __name__ == "__main__":
    main()
