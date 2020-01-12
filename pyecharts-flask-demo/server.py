from flask import Flask
from jinja2 import Markup, Environment, FileSystemLoader
from pyecharts.globals import CurrentConfig

# 关于 CurrentConfig，可参考 [基本使用-全局变量]
CurrentConfig.GLOBAL_ENV = Environment(loader=FileSystemLoader("./templates"))

from pyecharts import options as opts
from pyecharts.charts import Bar, Tree
import os
import json

app = Flask(__name__, static_folder="templates")


def bar_base() -> Bar:
    c = (
        Bar()
            .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
            .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
            .add_yaxis("商家B", [15, 25, 16, 55, 48, 8])
            .set_global_opts(title_opts=opts.TitleOpts(title="Bar-基本示例", subtitle="我是副标题"))
    )
    return c


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
    # 'emptyCircle', 'circle', 'rect', 'roundRect', 'triangle', 'diamond', 'pin', 'arrow', 'none'
    c = (
        Tree()
            .add("", data, orient="TB", symbol="rect", symbol_size=[40, 30], label_opts=opts.LabelOpts(
            position="inside",
            horizontal_align="right",
            vertical_align="middle",
            # rotate=-90,
            font_size=12,
            color='#00173d',
        ),
                 leaves_label_opts=opts.LabelOpts(position="inside")
                 )
            .set_global_opts(title_opts=opts.TitleOpts(title="Tree-基本示例"))
    )
    return c


def tree_tb() -> Tree:
    with open(os.path.join(r"C:\Users\49942\Desktop\danhuazhou-PyQt5-master\Myfile", "treemap.json"), "r",
              encoding="utf-8") as f:
        j = json.load(f)
        print(j)
        j = [
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
            .add(
            "",
            [j],
            collapse_interval=2,
            orient="TB",
            label_opts=opts.LabelOpts(
                position="top",
                horizontal_align="right",
                vertical_align="middle",
                rotate=-90,
            ),
        )
            .set_global_opts(title_opts=opts.TitleOpts(title="Tree-上下方向"))
    )
    return c


# @app.route("/")
# def index():
#     c = bar_base()
#     return Markup(c.render_embed())

@app.route("/")
def index():
    # c = tree_tb()
    c = tree_base()
    return Markup(c.render_embed())


if __name__ == "__main__":
    app.run(debug=True)
