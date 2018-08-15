import numpy as np
import numpy.random as np_random

print('对正数求和')
arr = np_random.randn(100)
print(arr)
print(arr >0)
print((arr > 0).sum()) # arr中大于0元素个数
print(arr[arr>0].sum()) # 大于0元素和
print()

print('对数组逻辑操作')
bools = np.array([False, False, True, False])
print(bools.any()) # 有一个为True则返回True
print(bools.all())# 有一个为False则返回False