# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 10:30:04 2021

@author: user
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

###csv 파일 분석
#os.getenv('HOME') +

# csv_file_path =  'C://aiffel//lms_9//trade_data.csv'

# trade = pd.read_csv(csv_file_path)

# # print('컬럼별 결측치 개수')
# # print(len(trade) - trade.count())

# trade = trade.drop('기�??�항',  axis = 1)
# # print(trade.head())

# # print(trade.isnull())
# # print(trade.isnull().any(axis=1))
# print([trade.isnull().any(axis=1)])

###정규화
# np.random.seed(2020)
# x = pd.DataFrame({'A' : np.random.randn(100)*4 + 4, 
#                           'B' : np.random.randn(100)-1})

# x_standardization = (x - x.mean())/x.std()

# x_min_max = (x -x.min())/(x.max() - x.min())

# fig, axs = plt.subplots(1,2, figsize=(12, 4),
#                         gridspec_kw={'width_ratios': [2, 1]})

# axs[0].scatter(x['A'], x['B'])
# axs[0].set_xlim(-5, 15)
# axs[0].set_ylim(-5, 5)
# axs[0].axvline(c='grey', lw=1)
# axs[0].axhline(c='grey', lw=1)
# axs[0].set_title('Original Data')

# axs[1].scatter(x_standardization['A'], x_standardization['B'])
# axs[1].set_xlim(-5, 5)
# axs[1].set_ylim(-5, 5)
# axs[1].axvline(c='grey', lw=1)
# axs[1].axhline(c='grey', lw=1)
# axs[1].set_title('Data after standardization')

# plt.show()

# fig, axs = plt.subplots(1,2, figsize=(12, 4),
#                         gridspec_kw={'width_ratios': [2, 1]})

# axs[0].scatter(x['A'], x['B'])
# axs[0].set_xlim(-5, 15)
# axs[0].set_ylim(-5, 5)
# axs[0].axvline(c='grey', lw=1)
# axs[0].axhline(c='grey', lw=1)
# axs[0].set_title('Original Data')

# axs[1].scatter(x_min_max['A'], x_min_max['B'])
# axs[1].set_xlim(-5, 5)
# axs[1].set_ylim(-5, 5)
# axs[1].axvline(c='grey', lw=1)
# axs[1].axhline(c='grey', lw=1)
# axs[1].set_title('Data after min-max scaling')

# plt.show()


### 구간화

salary = pd.Series([4300, 8370, 1750, 3830, 1840, 4220, 3020, 2290, 4740, 4600, 
                    2860, 3400, 4800, 4470, 2440, 4530, 4850, 4850, 4760, 4500, 
                    4640, 3000, 1880, 4880, 2240, 4750, 2750, 2810, 3100, 4290, 
                    1540, 2870, 1780, 4670, 4150, 2010, 3580, 1610, 2930, 4300, 
                    2740, 1680, 3490, 4350, 1680, 6420, 8740, 8980, 9080, 3990, 
                    4960, 3700, 9600, 9330, 5600, 4100, 1770, 8280, 3120, 1950, 
                    4210, 2020, 3820, 3170, 6330, 2570, 6940, 8610, 5060, 6370,
                    9080, 3760, 8060, 2500, 4660, 1770, 9220, 3380, 2490, 3450, 
                    1960, 7210, 5810, 9450, 8910, 3470, 7350, 8410, 7520, 9610, 
                    5150, 2630, 5610, 2750, 7050, 3350, 9450, 7140, 4170, 3090])


bins = [ 0, 2000, 4000, 6000, 8000, 10000]

ctg = pd.cut(salary, bins = bins)

#print('salary[0]', salary[0])
#print('salary]0]가 속한 카테고리 : ', ctg[0])

idx = ctg.value_counts().sort_index()

ctg2 = pd.qcut(salary, q = 5)

# print(ctg)
# print(ctg2)
#print(idx)

print(ctg2.value_counts().sort_index())

print(".\n.\n🛸 Well done!")