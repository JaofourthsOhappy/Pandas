import pandas as pd
import numpy as np

ndata = np.array([10,20,30,"Sittanat","Thai",True])
print(pd.Series(ndata))
# 0          10
# 1          20
# 2          30
# 3    Sittanat
# 4        Thai
# 5        True
# dtype: object
