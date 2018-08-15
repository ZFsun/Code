import numpy as np
import numpy.random as np_random

'''
zip可以接受任意多参数，然后重新组合成1个tuple列表。
zip([1, 2, 3], [4, 5, 6], [7, 8, 9])
返回结果：[(1, 4, 7), (2, 5, 8), (3, 6, 9)]
'''
print('通过真值表选择元素')
x_arr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
y_arr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])
result = [(x if c else y) for x, y, c in zip(x_arr, y_arr, cond)] # 通过列表推到实现
print(result)
print(np.where(cond, x_arr, y_arr))  # 使用NumPy的where函数
print()

print('更多where的例子')
arr = np_random.randn(4, 4)
print(arr)
print(np.where(arr > 0, 2, -2))
print(np.where(arr > 0, 2, arr))
print()

print('where嵌套')
cond_1 = np.array([True, False, True, True, False])
cond_2 = np.array([False, True, False, True, False])
# 传统代码如下
result = []
for i in range(len(cond)):
    if cond_1[i] and cond_2[i]:
        result.append(0)
    elif cond_1[i]:
        result.append(1)
    elif cond_2[i]:
        result.append(2)
    else:
        result.append(3)
print(result)
# np版本代码
result = np.where(cond_1 & cond_2, 0, \
          np.where(cond_1, 1, np.where(cond_2, 2, 3)))
print(result)

# 打印结果
"""
通过真值表选择元素
[1.1, 2.2, 1.3, 1.4, 2.5]
[1.1 2.2 1.3 1.4 2.5]

更多where的例子
[[ 0.361986    0.10591162  0.12547549  2.45894377]
 [ 0.49623549 -0.0808307  -0.9500051  -0.75954625]
 [ 0.18473737  0.46143021  1.09079355 -1.51982332]
 [ 0.2164365  -0.09363712 -0.15704795  0.52038058]]
[[ 2  2  2  2]
 [ 2 -2 -2 -2]
 [ 2  2  2 -2]
 [ 2 -2 -2  2]]
[[ 2.          2.          2.          2.        ]
 [ 2.         -0.0808307  -0.9500051  -0.75954625]
 [ 2.          2.          2.         -1.51982332]
 [ 2.         -0.09363712 -0.15704795  2.        ]]

where嵌套
[1, 2, 1, 0, 3]
[1 2 1 0 3]
请按任意键继续. . .
"""
