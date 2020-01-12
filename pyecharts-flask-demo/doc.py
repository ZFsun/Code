class Tree(
    # 初始化配置项，参考 `global_options.InitOpts`
    init_opts: opts.InitOpts = opts.InitOpts()
)

def add(
    # 系列名称，用于 tooltip 的显示，legend 的图例筛选。
    series_name: str,

    # 系列数据项
    data: Sequence[Union[opts.TreeItem, dict]],

    # 树图的布局，有 正交 和 径向 两种。这里的 正交布局 就是我们通常所说的水平 和 垂直 方向，
    # 对应的参数取值为 'orthogonal' 。而 径向布局 是指以根节点为圆心，每一层节点为环，
    # 一层层向外发散绘制而成的布局，对应的参数取值为 'radial'
    layout: str = "orthogonal",

    # 标记的图形。ECharts 提供的标记类型包括 'emptyCircle', 'circle', 'rect', 'roundRect',
    # 'triangle', 'diamond', 'pin', 'arrow', 'none'。
    symbol: str = "emptyCircle",

    # 标记的大小，可以设置成诸如 10 这样单一的数字，也可以用数组分开表示宽和高，
    # 例如 [20, 10] 表示标记宽为 20，高为 10。
    symbol_size: Numeric = 7,

    # 树图中 正交布局 的方向，也就是说只有在 layout = 'orthogonal' 的时候，
    # 该配置项才生效。对应有 水平 方向的 从左到右，从右到左；以及垂直方向的从上到下，
    # 从下到上。取值分别为 'LR' , 'RL', 'TB', 'BT'。注意，之前的配置项值 'horizontal'
    # 等同于 'LR'， 'vertical' 等同于 'TB'。
    orient: str = "LR",

    # tree组件离容器上侧的距离。
    # top 的值可以是像 20 这样的具体像素值，可以是像 '20%' 这样相对于容器高宽的百分比，
    # 也可以是 'top', 'middle', 'bottom'。
    # 如果 top 的值为'top', 'middle', 'bottom'，组件会根据相应的位置自动对齐。
    pos_top: Optional[str] = None,

    # tree 组件离容器左侧的距离。
    # left 的值可以是像 20 这样的具体像素值，可以是像 '20%' 这样相对于容器高宽的百分比，
    # 也可以是 'left', 'center', 'right'。
    # 如果 left 的值为'left', 'center', 'right'，组件会根据相应的位置自动对齐。
    pos_left: Optional[str] = None,

    # tree 组件离容器下侧的距离。
    # bottom 的值可以是像 20 这样的具体像素值，可以是像 '20%' 这样相对于容器高宽的百分比。
    pos_bottom: Optional[str] = None,

    # tree 组件离容器右侧的距离。
    # right 的值可以是像 20 这样的具体像素值，可以是像 '20%' 这样相对于容器高宽的百分比。
    pos_right: Optional[str] = None,

    # 折叠节点间隔，当节点过多时可以解决节点显示过杂间隔。
    collapse_interval: Numeric = 0,

    # 是否开启鼠标缩放和平移漫游。默认不开启。如果只想要开启缩放或者平移。
    # 可以设置成 'scale' 或者 'move'。设置成 true 为都开启
    is_roam: bool = False,

    # 子树折叠和展开的交互，默认打开 。由于绘图区域是有限的，而通常一个树图的节点可能会比较多，
    # 这样就会出现节点之间相互遮盖的问题。为了避免这一问题，可以将暂时无关的子树折叠收起，
    # 等到需要时再将其展开。如上面径向布局树图示例，节点中心用蓝色填充的就是折叠收起的子树，可以点击将其展开。
    # 注意：如果配置自定义的图片作为节点的标记，是无法通过填充色来区分当前节点是否有折叠的子树的。
    # 而目前暂不支持，上传两张图片分别表示节点折叠和展开两种状态。所以，如果想明确地显示节点的两种状态，
    # 建议使用 ECharts 常规的标记类型，如 'emptyCircle' 等。
    is_expand_and_collapse: bool = True,

    # 树图初始展开的层级（深度）。根节点是第 0 层，然后是第 1 层、第 2 层，... ，
    # 直到叶子节点。该配置项主要和 折叠展开 交互一起使用，目的还是为了防止一次展示过多节点，
    # 节点之间发生遮盖。如果设置为 -1 或者 null 或者 undefined，所有节点都将展开。
    initial_tree_depth: Optional[Numeric] = None,

    # 标签配置项，参考 `series_options.LabelOpts`
    label_opts: Union[opts.LabelOpts, dict] = opts.LabelOpts(),

    # 叶子节点标签配置项，参考 `series_options.LabelOpts`
    leaves_label_opts: Union[opts.LabelOpts, dict] = opts.LabelOpts(),

    # 提示框组件配置项，参考 `series_options.TooltipOpts`
    tooltip_opts: Union[opts.TooltipOpts, dict, None] = None,
)

class TreeItem(
    # 树节点的名称，用来标识每一个节点。
    name: Optional[str] = None,

                          # 节点的值，在 tooltip 中显示。
                          value

: Optional[Numeric] = None,

                      # 该节点的样式，参考 `series_options.LabelOpts`
                      label_opts: Optional[LabelOpts] = None,

                                                        # 子节点，嵌套定义。
                                                        children: Optional[Sequence] = None,
)

import json
import os

from pyecharts import options as opts
from pyecharts.charts import Page, Tree


def tree_base() -> Tree:
    data = [
        {
            "children": [
                {"name": "B"},
                {
                    "children": [
                        {"children": [{"name": "I"}], "name": "E"},
                        {"name": "F"},
                    ],
                    "name": "C",
                },
                {
                    "children": [
                        {"children": [{"name": "J"}, {"name": "K"}], "name": "G"},
                        {"name": "H"},
                    ],
                    "name": "D",
                },
            ],
            "name": "A",
        }
    ]
    c = (
        Tree()
        .add("", data)
        .set_global_opts(title_opts=opts.TitleOpts(title="Tree-基本示例"))
    )
    return c

def tree_lr() -> Tree:
    with open(os.path.join("fixtures", "flare.json"), "r", encoding="utf-8") as f:
        j = json.load(f)
    c = (
        Tree()
        .add("", [j], collapse_interval=2)
        .set_global_opts(title_opts=opts.TitleOpts(title="Tree-左右方向"))
    )
    return c

class InitOpts(
    # 图表画布宽度，css 长度单位。
    width: str = "900px",

    # 图表画布高度，css 长度单位。
    height: str = "500px",

    # 图表 ID，图表唯一标识，用于在多图表时区分。
    chart_id: Optional[str] = None,

    # 渲染风格，可选 "canvas", "svg"
    # # 参考 `全局变量` 章节
    renderer: str = RenderType.CANVAS,

    # 网页标题
    page_title: str = "Awesome-pyecharts",

    # 图表主题
    theme: str = "white",

    # 图表背景颜色
    bg_color: Optional[str] = None,

    # 远程 js host，如不设置默认为 https://assets.pyecharts.org/assets/"
    # 参考 `全局变量` 章节
    js_host: str = "",

    # 画图动画初始化配置，参考 `global_options.AnimationOpts`
    animation_opts: Union[AnimationOpts, dict] = AnimationOpts(),
)

class LabelOpts(
    # 是否显示标签。
    is_show: bool = True,

    # 标签的位置。可选
    # 'top'，'left'，'right'，'bottom'，'inside'，'insideLeft'，'insideRight'
    # 'insideTop'，'insideBottom'， 'insideTopLeft'，'insideBottomLeft'
    # 'insideTopRight'，'insideBottomRight'
    position: Union[str, Sequence] = "top",

    # 文字的颜色。
    # 如果设置为 'auto'，则为视觉映射得到的颜色，如系列色。
    color: Optional[str] = None,

    # 文字的字体大小
    font_size: Numeric = 12,

    # 文字字体的风格，可选：
    # 'normal'，'italic'，'oblique'
    font_style: Optional[str] = None,

    # 文字字体的粗细，可选：
    # 'normal'，'bold'，'bolder'，'lighter'
    font_weight: Optional[str] = None,

    # 文字的字体系列
    # 还可以是 'serif' , 'monospace', 'Arial', 'Courier New', 'Microsoft YaHei', ...
    font_family: Optional[str] = None,

    # 标签旋转。从 -90 度到 90 度。正值是逆时针。
    rotate: Optional[Numeric] = None,

    # 刻度标签与轴线之间的距离。
    margin: Optional[Numeric] = 8,

    # 坐标轴刻度标签的显示间隔，在类目轴中有效。
    # 默认会采用标签不重叠的策略间隔显示标签。
    # 可以设置成 0 强制显示所有标签。
    # 如果设置为 1，表示『隔一个标签显示一个标签』，如果值为 2，表示隔两个标签显示一个标签，以此类推。
    # 可以用数值表示间隔的数据，也可以通过回调函数控制。回调函数格式如下：
    # (index:number, value: string) => boolean
    # 第一个参数是类目的 index，第二个值是类目名称，如果跳过则返回 false。
    interval: Union[Numeric, str, None]= None,

    # 文字水平对齐方式，默认自动。可选：
    # 'left'，'center'，'right'
    horizontal_align: Optional[str] = None,

    # 文字垂直对齐方式，默认自动。可选：
    # 'top'，'middle'，'bottom'
    vertical_align: Optional[str] = None,

    # 标签内容格式器，支持字符串模板和回调函数两种形式，字符串模板与回调函数返回的字符串均支持用 \n 换行。
    # 模板变量有 {a}, {b}，{c}，{d}，{e}，分别表示系列名，数据名，数据值等。
    # 在 trigger 为 'axis' 的时候，会有多个系列的数据，此时可以通过 {a0}, {a1}, {a2} 这种后面加索引的方式表示系列的索引。
    # 不同图表类型下的 {a}，{b}，{c}，{d} 含义不一样。 其中变量{a}, {b}, {c}, {d}在不同图表类型下代表数据含义为：

    # 折线（区域）图、柱状（条形）图、K线图 : {a}（系列名称），{b}（类目值），{c}（数值）, {d}（无）
    # 散点图（气泡）图 : {a}（系列名称），{b}（数据名称），{c}（数值数组）, {d}（无）
    # 地图 : {a}（系列名称），{b}（区域名称），{c}（合并数值）, {d}（无）
    # 饼图、仪表盘、漏斗图: {a}（系列名称），{b}（数据项名称），{c}（数值）, {d}（百分比）
    # 示例：formatter: '{b}: {@score}'
    #
    # 回调函数，回调函数格式：
    # (params: Object|Array) => string
    # 参数 params 是 formatter 需要的单个数据集。格式如下：
    # {
    #    componentType: 'series',
    #    // 系列类型
    #    seriesType: string,
    #    // 系列在传入的 option.series 中的 index
    #    seriesIndex: number,
    #    // 系列名称
    #    seriesName: string,
    #    // 数据名，类目名
    #    name: string,
    #    // 数据在传入的 data 数组中的 index
    #    dataIndex: number,
    #    // 传入的原始数据项
    #    data: Object,
    #    // 传入的数据值
    #    value: number|Array,
    #    // 数据图形的颜色
    #    color: string,
    # }
    formatter: Optional[str] = None,

    # 在 rich 里面，可以自定义富文本样式。利用富文本样式，可以在标签中做出非常丰富的效果
    # 具体配置可以参考一下 https://www.echartsjs.com/tutorial.html#%E5%AF%8C%E6%96%87%E6%9C%AC%E6%A0%87%E7%AD%BE
    rich: Optional[dict] = None,
)