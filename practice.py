import pandas as pd
import numpy as np


시 = pd.Series([3, -8, 2, 0], index=['d', 'b', 'a', 'c'])
print(시)

시.reindex(['a', 'b', 'c', 'd', 'e'])