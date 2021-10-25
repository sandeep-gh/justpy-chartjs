from justpy_chartjs.tags import *
from justpy_chartjs import chartjscomponents as cj
import justpy as jp
from webapp_framework import display_units_reversed as dur
from justpy_chartjs.tags import cfg_template as ct
from addict import Dict
import functools

labels = ["ds1", "ds2", "ds3", "ds4", "ds5"]
datavals = [[{'x': 1, 'y': 3}, {'x': 5, 'y': 5}],
            [{'x': 1, 'y': 7}, {'x': 5, 'y': 2}],
            [{'x': 1, 'y': 0}, {'x': 5, 'y': 8}],
            [{'x': 1, 'y': 13}, {'x': 5, 'y': 2}],
            [{'x': 1, 'y': 2}, {'x': 5, 'y': 6}],
            [{'x': 1, 'y': 9}, {'x': 5, 'y': 7}],
            ]

cfgctx = Dict()
cfgctx.plttype = ct.PlotType.Line
cfgctx.xaxis_type = ct.ScaleType.Linear
cfgctx.xaxis_title = "xaxis"
cfgctx.yaxis_title = "yaxis"
cfgctx.plot_title = "testplot"
cfg = ct.build_pltcfg(cfgctx)
chartcfg = ct.build_cfg(cfg, labels, datavals)


my_chart_def = """{
              type: 'line',
              data: {
                  labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
                  datasets: [{
data: [5,6,7,8,9,10, 11]

}
], plugins: {
title : {text: "great title", display: true}},
              },
              options: {
                  scales: {
                      y: {
                          beginAtZero: true,
title: {text:"ayxis", display:true}
                      }

                  },

                  title: {
                      display: true,
                      text: 'Custom Chart Title',
position: 'bottom'
                  }
              }
          }"""

my_chart_def2 = """{
              type: 'bar',
              data: {
                  labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
                  datasets: [{
data: [5,6,7,8,9,10, 11]

}
]
              },
              options: {
                  scales: {
                      y: {
                          beginAtZero: true
                      }
                  },

                  title: {
                      display: true,
                      text: 'Custom Chart Title',
position: 'bottom'
                  }
              }
          }"""

labels = ["ds1", "ds2", "ds3", "ds4", "ds5"]
datavals = [[{'x': 1, 'y': 3}, {'x': 5, 'y': 5}],
            [{'x': 1, 'y': 7}, {'x': 5, 'y': 2}],
            [{'x': 1, 'y': 0}, {'x': 5, 'y': 8}],
            [{'x': 1, 'y': 13}, {'x': 5, 'y': 2}],
            [{'x': 1, 'y': 2}, {'x': 5, 'y': 6}],
            [{'x': 1, 'y': 9}, {'x': 5, 'y': 7}],
            ]

cfgctx = Dict()
cfgctx.plttype = ct.PlotType.Line
cfgctx.xaxis_type = ct.ScaleType.Linear
cfgctx.xaxis_title = "xaxis"
cfgctx.yaxis_title = "yaxis"
cfgctx.plot_title = "testplot"
cfg = ct.build_pltcfg(cfgctx)
chartcfg = ct.build_cfg(cfg, labels, datavals)


def wrapper(func):
    @functools.wraps(func)
    def run_func(*args, **kwargs):
        page = func(*args, **kwargs)
        print("got page ", page)
        page.act()
        return
    return run_func


def draw_chart():
    wp = jp.QuasarPage()
    wp.head_html = """<script src = "https://cdn.jsdelivr.net/npm/chart.js" > </script >\n <script src = "https://raw.githubusercontent.com/sandeep-gh/justpy-chartjs/main/justpy_chartjs/components/chartjs.js" > </script >\n    <link href = "https://unpkg.com/tailwindcss/dist/tailwind.min.css" rel = "stylesheet" >"""

    panel_pltcanvas_ = cj.ChartJS_("panel_canvas", pcp=[], options=chartcfg)
    dbref_canvas = panel_pltcanvas_(wp, "")

    @wrapper
    def change_plt(dbref, msg):
        print("in chage_plt")
        print("in chage_plt", dbref)
        print("in chage_plt", msg.page)
        #dbref_canvas.c.new_chart(msg.page, my_chart_def2)
        # dbref_canvas.chartjs.new_chart(my_chart_def2)
        #dbref_canvas.cjsbc.set_cfgattr("type", "bar")
        #dbref_canvas.cjsbc.set_cfgattr("options/scales/y/title/text", "bar")

        # await msg.page.update()
        return msg.page
    dbref_btn = dur.button_("abtn", "abtn", "abtn", change_plt)(wp, "")

    def act():
        dbref_canvas.chartjs.new_chart(my_chart_def2)
        pass
    wp.act = act

    return wp


app = jp.app
jp.justpy(draw_chart, start_server=False)
