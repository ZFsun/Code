# Pandas

### 基本功能

* 具备按轴自动或显式数据对齐功能的数据结构
* 集成时间序列功能
* 功能强大，灵活的分组功能对数据集执行拆分应用组合操作，以聚合和转换数据
* 使易于将其他Python和NumPy数据结构中的粗糙，不同索引的数据转换为DataFrame对象
* 直观的合并和连接数据集
* 既能处理时间序列数据也能处理非时间序列数据的数据结构
* 数学运算和约简（比如对某个轴求和）可以根据不同的元数据（轴编号）执行
* 灵活处理缺失数据
* 合并及其他出现在常见数据库（例如基于SQL的）中的关系型运算

### Pandas数据结构

Pandas数据结构构建在Numpy数组之上

* 序列(Series)，类似于一维数组的对象，它由一组数据（各种NumPy数据类型）
以及一组与之相关的数据标签（即索引）组成。
* 数据帧(DataFrame)，表格型的数据结构，它含有一组有序的列，每列可以是不同
的值类型（数值、字符串、布尔值等）。
* 面板(Panel)，三维ndarray创建pannel对象

#### Series（序列）

创建`pandas.Series(data, index=index)`

data可以是：

* python dict(字典)、
* ndarray、
* 标量值(如数字)

索引index是轴标签的列表。

data若为字典，在没有传入index参数时，字典的键将作为索引；若传入参数有index，则index作为索引。
data为ndarray时，索引必须要与数据长度相同，否则报错；未传递索引index的话，将创建0,1，...作为索引
data为标量时，必须传入index参数，该标量值将重复出现来匹配index长度。
`pandas.Series(data, name=name)`可以为Series命名，
`pandas.Series.rename()`方法可以位Series重命名，但所指对象会发生变化，如s2 = s.rename("different")，其中s与s2指向不同对象。

#### DataFrame（数据帧）

DataFrame接受数据类型：
* 一维数组，列表，字典或 Series 的字典
* 二维 numpy.ndarray
* 结构化或记录 ndarray
* Series
* 另一个DataFrame

可以选择传递index（行标签）和columns（列标签）参数

#### Panel（面板）

* items（条目）：轴0，每个条目对应于其中包含的DataFrame
* major_axis（主轴）：轴1，它是每个DataFrame的index（行）
* minor_axis（副轴）：轴2，它是每个DataFrames的columns（列）

#### 索引对象

pandas的索引对象负责管理轴标签和其他元数据
Index对象是不可修改的（immutable）

方法|说明
-----|------
append|append 连接另一个Index对象，产生一个新的Index。
diff|计算差集，并得到一个Index。
intersection|计算交集
union|计算并集
isin|计算一个指示各值是否包含在参数集合中的布尔型数组
delete|删除索引i处的元素，并得到新的Index。
drop|删除传入的值，并得到新的索引。
insert|将元素插入到索引i处，并得到新的Index
is_monotonic|当各元素均大于等于前一个元素时，返回True。
is_unique|当Index没有重复值时，返回True。
unique|计算Index中唯一值得数组

重新索引，创建一个适应新索引的新对象，该Series的reindex将会根据新索引进行重排。如果某个索引值当前不存在，就引入缺失值




