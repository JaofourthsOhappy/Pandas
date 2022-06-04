from turtle import color
import pandas as pd

colors = {"Green":"Mango","Red":"apple","Yellow":"Papaya"}
print(pd.Series(colors))
# Green      Mango
# Red        apple
# Yellow    Papaya
# dtype: object

age = {"John":50,"Chai":34,"sarug":45}
print(pd.Series(age))
# John     50
# Chai     34
# sarug    45
# dtype: int64