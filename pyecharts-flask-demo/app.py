from random import randrange

from flask import Flask, render_template

from pyecharts import options as opts
from pyecharts.charts import Bar, Tree
import os

app = Flask(__name__, static_folder="templates")


# app.debug = True

def bar_base() -> Bar:
    c = (
        Bar()
            .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
            .add_yaxis("商家A", [randrange(0, 100) for _ in range(6)])
            .add_yaxis("商家B", [randrange(0, 100) for _ in range(6)])
            .set_global_opts(title_opts=opts.TitleOpts(title="Bar-基本示例", subtitle="我是副标题"))
    )
    return c


def tree_tb() -> Tree:
    with open(os.path.join("fixtures", "flare.json"), "r", encoding="utf-8") as f:
        j = json.load(f)
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


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/barChart")
def get_bar_chart():
    c = bar_base()
    return c.dump_options_with_quotes()


if __name__ == "__main__":
    app.run(debug=True)
