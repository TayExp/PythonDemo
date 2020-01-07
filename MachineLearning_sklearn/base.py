import numpy as np
import matplotlib.pylab as plt
from sklearn.cluster import KMeans
# from scipy import spatial
# print(spatial.distance.cdist(np.asarray([[1]]),np.asarray([[-1]]),metric='euclidean'))
from sklearn.datasets import load_iris

iris = load_iris()
# print(type(iris)) # <class 'sklearn.utils.Bunch'>
# print(type(iris.data)) # <class 'numpy.ndarray'>

y = iris.target
X = iris.data[:, 2:4] #表示我们只取特征空间中的后两个维度
print(X.shape) #绘制数据分布图
plt.scatter(X[:, 0], X[:, 1], c = "red", marker='o', label='see')
plt.xlabel('petal length')
plt.ylabel('petal width')
plt.legend(loc=2)
plt.show()

estimator = KMeans(n_clusters=3)#构造聚类器
estimator.fit(X)#聚类
label_pred = estimator.labels_ #获取聚类标签
lable = estimator.fit_predict(X)
# 绘制k-means结果
x0 = X[label_pred == 0]
x1 = X[label_pred == 1]
x2 = X[label_pred == 2]
plt.scatter(x0[:, 0], x0[:, 1], c = "red", marker='o', label='label0')
plt.scatter(x1[:, 0], x1[:, 1], c = "green", marker='*', label='label1')
plt.scatter(x2[:, 0], x2[:, 1], c = "blue", marker='+', label='label2')
plt.xlabel('petal length')
plt.ylabel('petal width')
plt.legend(loc=2)
plt.show()