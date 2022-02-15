from xml.dom import WrongDocumentErr
import pandas as pd
import numpy as np
import openpyxl as opxl
wrinkle_data = pd.read_excel('G:/내 드라이브/Yuchang-Practice/Data_coding_ver.xlsx')

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