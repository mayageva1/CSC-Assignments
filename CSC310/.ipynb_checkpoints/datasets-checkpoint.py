import pandas as pd
dataset_list = [{'url': 'https://raw.githubusercontent.com/MainakRepositor/Datasets/master/Pokemon.csv', # a dataset with nonnumerical data in at least one column
     'name': 'pokemon_df',
     'load_func':  pd.read_csv},
     {'url': 'https://raw.githubusercontent.com/MainakRepositor/Datasets/master/parks.csv', #any dataset you're interested in
     'name': 'parks_df',
     'load_func': pd.read_csv},
     {'url': 'https://raw.githubusercontent.com/MainakRepositor/Datasets/master/Github_Stats/issues.csv', #any dataset you're interested in
     'name': 'issues_df',
     'load_func': pd.read_csv}]