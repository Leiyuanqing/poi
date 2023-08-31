import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

font = {'family': 'SimHei',
        'weight': 'bold',
        'size': '16'}
plt.rc('font', **font)
plt.rc('axes', unicode_minus=False)

df = pd.read_json('C:\\Users\\M17\\Desktop\\test.json', orient='records')
print(df)
X = np.array(df[['lng', 'lat']])
y = np.array(df['types'])
# 可视化


plt.figure(figsize=(10, 10))  # 设置画布
# 绘制每个类别的散点图
# plt.scatter(X[y == 0][:, 0], X[y == 0][:, 1], label='美食')
# plt.scatter(X[y == 1][:, 0], X[y == 1][:, 1], label='丽人')
# plt.scatter(X[y == 2][:, 0], X[y == 2][:, 1], label='休闲')
# plt.scatter(X[y == 3][:, 0], X[y == 3][:, 1], label='生活')
# plt.scatter(X[y == 4][:, 0], X[y == 4][:, 1], label='结婚')
# plt.scatter(X[y == 5][:, 0], X[y == 5][:, 1], label='亲子')
# plt.scatter(X[y == 6][:, 0], X[y == 6][:, 1], label='运动')
plt.scatter(X[y == 7][:, 0], X[y == 7][:, 1], label='家装')
# plt.scatter(X[y == 8][:, 0], X[y == 8][:, 1], label='学习')
# plt.scatter(X[y == 9][:, 0], X[y == 9][:, 1], label='医疗')

plt.title("家装")
# plt.legend()  # 生成图例
plt.show()
