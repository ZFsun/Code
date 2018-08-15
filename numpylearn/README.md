# NumPy
### Ndarray创建

NumPy 中定义的最重要的对象是称为 ndarray 的 N 维数组类型。

创建语法：numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)

参数|说明
---|---
object|数据
dtype|数组数据类型
copy|对象是否被复制，默认true
order|C(按行)、F(按列)或A(任意，默认)
subok|默认情况下，返回的数组被强制为基类数组。 如果为true，则返回子类。
ndimin|指定返回数组的最小维数
常见生成ndarray函数：zeros(),zeros_like(),ones(),ones_like(),empty(),empty_like(),eye(),identity().
* numpy.zeros(shape, dtype=float, order='C') 生成数组数据全为0
* numpy.zeros_like(a, dtype=None, order='K', subok=True) 模仿a(形状和类型)生成全为0数组。subok为True然后新创建的数组将使用a的子类类型，否则否则它将是一个基类数组。
* numpy.eye(N, M=None, k=0, dtype=<class 'float'>, order='C')生成N*M(默认N=M)矩阵。参数k默认为0，输出的是对角线全“1”，其余全“0”的方阵，如果k为正整数，则在右上方第k条对角线全“1”其余全“0”，k为负整数则在左下方第k条对角线全“1”其余全“0”。
* numpy.identity(n, dtype=None) 生成对角线矩阵，与eye类似。


### NumPy数据类型
数据类型|描述
----|-----
int8|有符号8位整型
uint8|无符号8位整型
int16|有符号16位整型
uint16|无符号16位整型
int32|有符号32位整型
uint32|无符号32位整型
int64|有符号64位整型
uint64|无符号64位整型
float16|半精度浮点数,符号位，5位指数，10位尾数。
float32|标准的单精度浮点数。1符8指23尾。
float64|标准的双精度浮点数。1符11指52尾。
float128|扩展精度浮点数
complex64|复数，由两个 32 位浮点表示(实部和虚部) 
complex128|复数，由两个 64 位浮点表示(实部和虚部) 
complex256|复数，由两个 128 位浮点表示(实部和虚部) 
bool|布尔类型
object|Python对象类型
string_|固定长度的字符串类型
unicode_|固定长度的unicode类型

### Ndarray数组运算
*  大小相等的数组之间的任何算术运算都会将运算应用到元素级
*  数组与标量的算术运算也会将那个标量值传播到各个元素
*  当两个数组形状不同是会使用**广播**功能，较小的数组会广播到较大数组的大小，以便使它们的形状可兼容。

### Ndarray索引与切片

*  普通索引
*  布尔索引（利用布尔数组索引）
*  花式索引（利用整数数组进行索引）

切片参数：起始位置、结束位置，步长

### 转置和轴对换

*  一维／二维数组转置
*  高维数组轴对换

### Ndarray函数

函数|说明
-----|------
abs, fabs|计算整数、浮点数或复数的绝对值。对于非复数值，可以使用更快的fabs。
sqrt|计算各元素的平方根。相当于arr ** 0.5
sqare|计算各元素的平方。相当于arr ** 2
exp|计算各元素的e^x
log, log10, log2, log1p|分别为自然对数、底数为10的log、底数为2的log和log(1 + x)
sign|计算各元素的正负号：1（正数）、0（零）、－1（负数）。
ceil|计算各元素的ceiling值，即大于等于该值的最小整数。
floor|计算各元素的floor值，即小于等于该值的最小整数。
rint|将各元素值四舍五入到最接近的整数，保留dtype。
modf|将数组的小数部分与整数部分以两个独立数组的形式返还。
isnan|返回一个表示“哪些值是NaN（这不是一个数字）”的布尔型数组
isfinite, isinf|分别返回一个表示“哪些元素是有限的（非inf，非NaN）”或“哪些元素是无穷的”的布尔型数组
cos,cosh,sin,sinh,tan,tanh|普通型或双曲型三角函数
arccos,arccosh,arcsin,arcsinh,arctan,arctanh|反三角函数
logical_not|计算各元素not x的真值。相当于-arr。
add|将数组中对应的元素相加
subtract|从第一个数组中减去第二个数组中的元素
multiply|数组元素相乘
divide, floor_divide|除法或向下取整除法
power|对第一个数组中的元素A和第二个数组中对应位置的元素B，计算A^B。
maximum, fmax|元素级的最大值计算。fmax将忽略NaN
minimum, fmin|元素级的最小值计算。fmin将忽略NaN。
mod|元素级的求模计算
copysign|将第二个数组中的符号复制给第一个数组中的值
greater,greater_equal,less, less_equal,equal,not_equal|执行元素级的比较，最终产生布尔型数组。
logical_and,logical_or,logical_xor|执行元素级的真值逻辑运算，最终产生布尔型数组

### 数学和统计方法

函数|说明
-----|-----
sum|对数组中全部或某轴向的元素求和。零长度的数组的sum为0。
mean|算术平均数。零长度的数组的mean为NaN。
std,var|分别为标准差和方差，自由度可调（默认为n）。
min,max|最大值和最小值
argmin|分别为最大值和最小值的索引
cumsum|所有元素的累计和
cumprod|所有元素的累计积

### 排序

*  numpy.sort()，函数返回输入数组的排序副本
*  numpy.argsort()，函数对输入数组沿给定轴执行间接排序，并使用指定排序类型返回数据的索引数组。 这个索引数组用于构造排序后的数组。即返回一串索引按索引可以进行排序。
*  numpy.lexsort()，函数使用键序列执行间接排序。 键可以看作是电子表格中的一列。 该函数返回一个索引数组，使用它可以获得排序数据。

### 去重

函数|说明
-----|-----
unique(x)|计算x中的唯一元素，并返回有序结果。
intersect1d(x, y)|计算x和y中的公共元素，并返回有序结果。
union1d(x, y)|计算x和y的并集，并返回有序结果。
in1d(x, y)|得到一个表述"x的元素是否包含于y"的布尔型数组
setdiff1d(x, y)|集合的差，即元素在x中且不在y中
setxor1d(x, y)|集合的异或，即存在于一个数组中但不同时存在于两个数组中的元素

### 文件操作

*  load()和save()函数处理 numPy 二进制文件(带npy扩展名)
*  loadtxt()和savetxt()函数处理正常的文本文件

### 线性代数

函数|说明
-----|-----
diag|以一维数组的形式返回方阵的对角线（或非对角线元素），获将一维数组转换为方阵（非对角线元素为0）。
dot|矩阵乘法
trace|计算对角线元素的和
det|计算矩阵行列式
eig|计算方阵的特征值和特征向量
inv|计算方阵的逆
pinv|计算矩阵的Moore-Penrose伪逆
qr|计算QR分解
svd|计算奇异值分解
solve|解线性方程Ax = b，其中A为一个方阵
lstsq|计算Ax = b的最小二乘解

### 随机数生成

函数|说明
-----|------
seed|确定随机数生成器的种子
permutation|返回一个序列的随机排列或返回一个随机排列的返回
shuffle|对一个序列就地随机乱序
rand|产生均匀分布的样本值
randint|从给定的上下限范围内随机选取整数
randn|产生正态分布（平均值为0，标准差为1）
binomial|产生二项分布的样本值
normal|产生正态（高斯）分布的样本值
beta|产生Beta分布的样本值
chisquare|产生卡方分布的样本值
gamma|产Gamma分布的样本值
uniform|产生在[0, 1]中均匀分布的样本值

### 数组的合并与拆分

函数|说明
----|-----
concatenate|最一般化的连接，沿一条轴连接一组数组
vstack, row_stack|以面向行的方式对数组进行堆叠（沿轴0）
hstack|以面向行的方式对数组进行堆叠（沿轴1）
column_stack|类似于hstack，但是会先将一维数组转换为二维列向量
dstack|以面向“深度”的方式对数组进行堆叠（沿轴2）
split|沿指定轴在指定的位置拆分数组
hsplit, vsplit, dsplit|split的便捷化函数，分别沿着轴0、轴1和轴2进行拆分。

官方文档：https://docs.scipy.org/doc/numpy/genindex.html

