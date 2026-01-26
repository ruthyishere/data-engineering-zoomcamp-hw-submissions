import inspect
import pandas as pd
import itertools 

# # 1. See signature
# print(inspect.signature(pd.read_csv))

kwargs = {
    'filepath_or_buffer': 'some_path.csv',
    'sep': ',',
    'header': 'infer',
    'names': None,
    'yasskaween': 'hello',
    'fake_param': 123
}

# 2. Get parameter names only

filtered_kwargs = filter(lambda k: k in inspect.signature(pd.read_csv).parameters.keys(), kwargs.keys())
print(list(filtered_kwargs))

# # 3. Classic help
# help(pd.read_csv)

# # 4. Just the docstring
# print(pd.read_csv.__doc__)

