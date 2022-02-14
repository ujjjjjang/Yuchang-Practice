from xml.dom import WrongDocumentErr
import pandas as pd
import numpy as np
import openpyxl

wrinkle_data = pd.read_excel('G:/내 드라이브/Yuchang-Practice/Data_coding_ver.xlsx')

wrinkle1 = wrinkle_data.filter(['W101', 'W102', 'W103', 'W104'])
#put 'W_Total' in column. W_Total is added result of W101 to W104

type("W101")
print("W101")
print(wrinkle_data['W101'])

#output

# W101
# 1: 0 <= x < 17.89
# 2: 17.89 <= x < 22.34
# 3: 22.34 <= x
# W102
# 1: 0 <= x < 157.83
# # 2: 157.83 <= x < 213.25
# 3: 213.25 <= x
# W103
# 1: 0 <= x < 21.19
# 2: 21.19 <= x < 27.75
# 3: 27.75 <= x
# W104
# 1: 0 <= x < 155.36
# 2: 155.36 <= x < 206.54
# 3: 206.54 <= x