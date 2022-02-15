from xml.dom import WrongDocumentErr
import pandas as pd
import numpy as np
import openpyxl as opxl
wrinkle_data = pd.read_excel('G:/내 드라이브/Yuchang-Practice/Data_coding_ver.xlsx')
#put 'W_Total' in column. W_TOTAL is added result of W101 to W104
W1 = []
for i in wrinkle_data['W101']:
    if 0 <= i and i < 17.89 : W1.append(1)
    elif 17.89 <= i and i < 22.34 : W1.append(2)
    else : W1.append(3)
W2 = []
for i in wrinkle_data['W102']:
    if 0 <= i and i < 157.83 : W2.append(1)
    elif 157.83 <= i and i < 213.25 : W2.append(2)
    else : W2.append(3)
W3 = []
for i in wrinkle_data['W103']:
    if 0 <= i and i < 21.19 : W3.append(1)
    elif 21.19 <= i and i < 27.75 : W3.append(2)
    else : W3.append(3)
W4 = []
for i in wrinkle_data['W104']:
    if 0 <= i and i < 155.36 : W4.append(1)
    elif 155.36 <= i and i < 206.54 : W4.append(2)
    else : W4.append(3)

W_Total = []
for i in range(0, len(W1)):
     W_Total.append(W1[i] + W2[i] + W3[i] + W4[i])

print(W_Total)
#output
#print(wrinkle_data.filter(['W101', 'W102', 'W103', 'W104','W_TOTAL']))



# W101
# 1: 1 if 0 <= x < 17.89
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