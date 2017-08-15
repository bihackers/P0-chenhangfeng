# -*- coding:UTF-8 -*-

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

# 0、导入数据集
df = pd.read_excel('stroopdata.xlsx', 'stroopdata')

# 1、直方图
fig = plt.figure()
ax = fig.add_subplot(111)
ax.hist(df['D'], bins=7)
plt.title('D distribution')
plt.xlabel('D')
plt.ylabel('num')
plt.show()

# 2、箱线图  
fig = plt.figure()
ax = fig.add_subplot(111)
ax.boxplot(df['D'])
plt.show()