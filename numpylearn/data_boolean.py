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

# 打印结果
"""
对正数求和
[ 1.85048889 -0.27223344  0.81564672  0.85403426  0.83271564 -0.80139679
  0.10916926  0.75795019 -0.7509345  -1.10042115 -0.36823207  1.78331088
  0.41522733 -0.07143896 -0.0581272  -0.50169517  0.83660618  0.01775113
 -1.43505196  0.4751372  -0.44289952 -0.04693219 -0.29435335  1.11175895
 -2.84249693  0.87349309  0.11244942  0.78589871  0.3242563   0.17465209
  1.18967526 -0.26086766 -0.41095136  0.02394412 -0.24018606 -0.22071156
  1.78837391  0.12582019  0.63164719 -1.54511083 -1.2537518   2.26900015
 -0.0751325  -1.41693817 -3.23261001  0.9247589  -0.31019194 -0.18521902
 -0.13623468  0.77023708 -0.64361438 -0.11915692 -0.01613932 -1.42149683
 -0.49858854 -1.16843454 -1.99158436  0.28872133 -1.91279793  3.35636945
 -0.29165175  0.70767381  1.58823484 -0.34762437  1.83722383  1.16115507
 -1.77959607  1.23851637 -0.87236054  0.12474073  0.59695118 -0.45248999
 -0.53271491  1.16585484  1.16469485 -0.30846758 -0.08660459  1.32171886
 -0.10347756  0.5515532  -1.1423264  -1.54447033  1.47602687 -1.8016174
 -0.27977088 -0.09865536  0.9992948   0.49914794  1.32851155 -1.34123066
 -1.18895037  0.99870779 -0.6031933  -0.65959939  0.5403386   0.08396481
  0.96479645 -0.80189565  1.17444853 -0.66401812]
[ True False  True  True  True False  True  True False False False  True
  True False False False  True  True False  True False False False  True
 False  True  True  True  True  True  True False False  True False False
  True  True  True False False  True False False False  True False False
 False  True False False False False False False False  True False  True
 False  True  True False  True  True False  True False  True  True False
 False  True  True False False  True False  True False False  True False
 False False  True  True  True False False  True False False  True  True
  True False  True False]
47
43.02264874425132

对数组逻辑操作
True
False

请按任意键继续. . .
"""