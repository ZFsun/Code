import numpy as np

"""
创建Numpy数组
"""

print('使用普通一维数组生成NumPy一维数组')
data = [1, 2, 3.2, 4, 7]
arr = np.array(data)
print(arr)
print('元素类型:',arr.dtype)
print()


print('使用普通二维数组生成NumPy二维数组')
data = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr = np.array(data)
print(arr)
print('数组维度:',arr.shape)
print()

"""
zeros(),zeros_like(),ones(),ones_like(),empty(),empty_like(),
"""
print('使用zeros/empty')
# 语法格式numpy.zeros(shape, dtype=float, order='C')
print(np.zeros(6)) # 生成包含6个0的一维数组
print(np.zeros((3, 6))) # 生成3*6的二维数组
print(np.zeros_like(arr)) # 根据arr数组形状与类型创建数据全为0的数组
print(np.empty((2, 3, 2))) # 生成2*3*2的三维数组，所有元素未初始化。注意与zeros区分。
print(np.eye(5,5,1)) # 生成N*M（默认N=M）对角线矩阵，第三个参数指定对角线位置。
print(np.identity(5)) # 生成N*N对角线矩阵
print()

print('使用arrange生成连续元素')
print(np.arange(15))  # [0, 1, 2, ..., 14]

# 打印结果
"""
使用普通一维数组生成NumPy一维数组
[1.  2.  3.2 4.  7. ]
元素类型: float64

使用普通二维数组生成NumPy二维数组
[[1 2 3 4]
 [5 6 7 8]]
数组维度: (2, 4)

使用zeros/empty
[0. 0. 0. 0. 0. 0.]
[[0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0.]]
[[0 0 0 0]
 [0 0 0 0]]
[[[1.81064342e-295 2.13945865e+161]
  [4.59220660e-072 5.98129763e-154]
  [1.06758000e+224 4.46811730e-091]]

 [[5.98149672e-154 7.50187034e+247]
  [1.96097649e+243 3.03736202e+180]
  [3.55455412e+180 6.01347002e-154]]]
[[0. 1. 0. 0. 0.]
 [0. 0. 1. 0. 0.]
 [0. 0. 0. 1. 0.]
 [0. 0. 0. 0. 1.]
 [0. 0. 0. 0. 0.]]
[[1. 0. 0. 0. 0.]
 [0. 1. 0. 0. 0.]
 [0. 0. 1. 0. 0.]
 [0. 0. 0. 1. 0.]
 [0. 0. 0. 0. 1.]]

使用arrange生成连续元素
[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]
请按任意键继续. . .
"""