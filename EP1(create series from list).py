import pandas as pd

data_list = [10,20,30,"Sittanat","Thai",True]

print(data_list)
# [10, 20, 30, 'Sittanat', 'Thai', True]

print(pd.Series(data_list))
# 0          10
# 1          20
# 2          30
# 3    Sittanat
# 4        Thai
# 5        True
# dtype: object