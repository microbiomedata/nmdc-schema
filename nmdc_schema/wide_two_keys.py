import pandas as pd

wide_two_keys_path = "../wide_two_keys.csv"

wide_two_keys = pd.read_csv(wide_two_keys_path, sep='\t', dtype=str)

# wide_two_keys['first_last'] = wide_two_keys['first'] + "_" + wide_two_keys['last']

wide_two_keys_melted = pd.melt(wide_two_keys, id_vars=['first', 'last'], var_name='key', value_name='value')

wide_two_keys_melted['last_key'] = wide_two_keys_melted['last'] + "_" + wide_two_keys_melted['key']

wide_data = wide_two_keys_melted.pivot(index='first', values='value', columns='last_key')

wide_data.to_clipboard()

print(wide_data)
