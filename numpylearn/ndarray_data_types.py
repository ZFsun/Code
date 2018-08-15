import numpy as np

"""
数组数据类型指定与修改
"""

print('生成数组时指定数据类型')
arr = np.array([1, 2, 3], dtype = np.string_)
print(arr.dtype)
print()


print('使用astype复制数组并转换数据类型')
int_arr = np.array([1, 2, 3, 4, 5])
float_arr = int_arr.astype(np.float)
print(int_arr.dtype)
print(float_arr.dtype)
print()
# 注意使用astype将float转换为int时小数部分将被舍弃


print('使用astype把字符串数组转换为数组数组，如果失败抛出异常。')
str_arr = np.array(['1.25', '-9.6', '42'], dtype = np.string_)
float_arr = str_arr.astype(dtype = np.float)
print(float_arr)
print()


# 打印结果
"""
生成数组时指定数据类型
float64

使用astype复制数组并转换数据类型
int32
float64

使用astype把字符串数组转换为数组数组，如果失败抛出异常。
[ 1.25 -9.6  42.  ]

"""