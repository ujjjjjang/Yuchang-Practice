import pandas as pd
from pandas import DataFrame

data = pd.read_excel('G:/내 드라이브/Yuchang-Practice/Data_coding_ver.xlsx')
W1 = []
for i in data['W101']:
    if 0 <= i and i < 17.89 : W1.append(1)
    elif 17.89 <= i and i < 22.34 : W1.append(2)
    else : W1.append(3)
W2 = []
for i in data['W102']:
    if 0 <= i and i < 157.83 : W2.append(1)
    elif 157.83 <= i and i < 213.25 : W2.append(2)
    else : W2.append(3)
W3 = []
for i in data['W103']:
    if 0 <= i and i < 21.19 : W3.append(1)
    elif 21.19 <= i and i < 27.75 : W3.append(2)
    else : W3.append(3)
W4 = []
for i in data['W104']:
    if 0 <= i and i < 155.36 : W4.append(1)
    elif 155.36 <= i and i < 206.54 : W4.append(2)
    else : W4.append(3)
W_Total = []
for i in range(0, len(W1)):
     W_Total.append(W1[i] + W2[i] + W3[i] + W4[i])

A1 = []
for i in data['A101']:
    if 0 <= i and i < 61.53 : A1.append(3)
    elif 61.53 <= i and i < 70.07 : A1.append(2)
    else : A1.append(1)
A2 = []
for i in data['A102']:
    if 0 <= i and i < 67.46 : A2.append(3)
    elif 67.46 <= i and i < 73.67 : A2.append(2)
    else : A2.append(1)
A_Total = []
for i in range(0, len(A1)):
     A_Total.append(A1[i] + A2[i])
    
M1 = []
for i in data['M101']:
    if 0 <= i and i < 148.33 : M1.append(1)
    elif 148.33 <= i and i < 179.00 : M1.append(2)
    else : M1.append(3)
M2 = []
for i in data['M102']:
    if 0 <= i and i < 106.00 : M2.append(1)
    elif 106.00 <= i and i < 131.00 : M2.append(2)
    else : M2.append(3)
R1 = []
for i in data['R201']:
    if 0 <= i and i < 58.81 : R1.append(3)
    elif 58.81 <= i and i < 60.93 : R1.append(2)
    else : R1.append(1)
R2 = []
for i in data['R202']:
    if 0 <= i and i < 62.34 : R2.append(3)
    elif 62.34 <= i and i < 64.34 : R2.append(2)
    else : R2.append(1)
M_Total = []
for i in range(0, len(M1)):
     M_Total.append(M1[i] + M2[i] + R1[i] + R2[i])

L1 = []
for i in data['L101']:
    if 0 <= i and i < 52.00 : L1.append(1)
    elif 52.00 <= i and i < 92.33 : L1.append(2)
    else : L1.append(3)
L2 = []
for i in data['L102']:
    if 0 <= i and i < 27.00 : L2.append(1)
    elif 27.00 <= i and i < 51.00 : L2.append(2)
    else : L2.append(3)
L_Total = []
for i in range(0, len(L1)):
     L_Total.append(L1[i] + L2[i])

S = []
for i in data['S101']:
    if i == '민감':
        S.append(2)
    else:
        S.append(1)
S_Total = []
for i in range(0, len(S)):
     S_Total.append(S[i])

Total = DataFrame({"W_Total": W_Total,'A_Total': A_Total, 'M_Total': M_Total, 'L_Total':L_Total, 'S_Total':S_Total})
write = pd.ExcelWriter('jeju_total_sum.xlsx', engine='xlsxwriter')
Total.to_excel(write,sheet_name='Sheet1',index=False)
write.close()