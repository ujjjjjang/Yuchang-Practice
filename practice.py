import numpy as np
import pandas as pd


data = [[1,10,100],[2,20,200],[3,30,300]]
col = ['col1','col2','col3']
row = ['row1','row2','row3']
df = pd.DataFrame(data=data,index=row,columns=col)

data2  = [[3],[4],[5]]
df2 = pd.DataFrame(data=data2,index=['row1','row2','row3'],columns=['col1'])
result = df.sub(df2)
print(result)