import pandas as pd
import numpy as np
from sklearn.cluster import KMeans, SpectralClustering
import matplotlib.pyplot as plt

df = pd.read_json('C:\\Users\\M17\\Desktop\\test.json', orient='records')
print(df)

X = np.array(df[['lng', 'lat']])
# km = KMeans(n_clusters=10).fit(X)
km = SpectralClustering(n_clusters=10, affinity='nearest_neighbors', assign_labels='kmeans').fit(X)
print(km.labels_)

# 可视化


plt.figure(figsize=(10, 10))  # 设置画布
# 绘制每个类别的散点图
plt.scatter(X[km.labels_ == 0][:, 0], X[km.labels_ == 0][:, 1], label='0')
plt.scatter(X[km.labels_ == 1][:, 0], X[km.labels_ == 1][:, 1], label='1')
plt.scatter(X[km.labels_ == 2][:, 0], X[km.labels_ == 2][:, 1], label='2')
plt.scatter(X[km.labels_ == 3][:, 0], X[km.labels_ == 3][:, 1], label='3')
plt.scatter(X[km.labels_ == 4][:, 0], X[km.labels_ == 4][:, 1], label='4')
plt.scatter(X[km.labels_ == 5][:, 0], X[km.labels_ == 5][:, 1], label='5')
plt.scatter(X[km.labels_ == 6][:, 0], X[km.labels_ == 6][:, 1], label='6')
plt.scatter(X[km.labels_ == 7][:, 0], X[km.labels_ == 7][:, 1], label='7')
plt.scatter(X[km.labels_ == 8][:, 0], X[km.labels_ == 8][:, 1], label='8')
plt.scatter(X[km.labels_ == 9][:, 0], X[km.labels_ == 9][:, 1], label='9')

plt.title("kmeans")
plt.legend()  # 生成图例
plt.show()
