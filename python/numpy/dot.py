import numpy as np

X = np.ones(25).reshape((5, 5))
X[:, 2] *= 2
y = np.arange(1, 6)
print(X, y)
'''
      [[1. 1. 2. 1. 1.]
       [1. 1. 2. 1. 1.]
       [1. 1. 2. 1. 1.]
       [1. 1. 2. 1. 1.]
X =    [1. 1. 2. 1. 1.]]      y = [1 2 3 4 5]
'''

dot1 = np.dot(y, X)
print(dot1)  # [15. 15. 30. 15. 15.]

dot2 = np.dot(X.T, y)
print(dot2)  # [15. 15. 30. 15. 15.]

# 这说明ndarray既可以作为行向量也可以作为列向量，会根据与其点乘的矩阵的形式自动判断该选取哪一种
