import pandas as pd

items = ["Mango","Banana","Orange"]
idx = [50,20,30]

print(pd.Series(items,index=idx))
# 50     Mango
# 20    Banana
# 30    Orange
# dtype: object