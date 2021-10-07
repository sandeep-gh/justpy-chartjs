from  jpcjs_tags import *
from  justpy_chartjs import chartjscomponents as cj
#import chartjscomponents as cj
import justpy as jp
import json
import display_components as dc
import display_units_reversed as dur
import tailwind_style_tags as ddt

import jpcjs_tags.cfg_template as ct
from addict import Dict
import jpcjs_tags.cfg_template as ct
from addict import Dict

labels = ["ds1", "ds2", "ds3", "ds4", "ds5"]
datavals = [ [{'x': 1, 'y':3}, {'x':5, 'y':5}],
             [{'x': 1, 'y':7}, {'x':5, 'y':2}],
             [{'x': 1, 'y':0}, {'x':5, 'y':8}],
             [{'x': 1, 'y':13}, {'x':5, 'y':2}],
             [{'x': 1, 'y':2}, {'x':5, 'y':6}],
             [{'x': 1, 'y':9}, {'x':5, 'y':7}],
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
              type: 'line',
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
datavals = [ [{'x': 1, 'y':3}, {'x':5, 'y':5}],
             [{'x': 1, 'y':7}, {'x':5, 'y':2}],
             [{'x': 1, 'y':0}, {'x':5, 'y':8}],
             [{'x': 1, 'y':13}, {'x':5, 'y':2}],
             [{'x': 1, 'y':2}, {'x':5, 'y':6}],
             [{'x': 1, 'y':9}, {'x':5, 'y':7}],
    ]

cfgctx = Dict()
cfgctx.plttype = ct.PlotType.Line
cfgctx.xaxis_type = ct.ScaleType.Linear
cfgctx.xaxis_title = "xaxis"
cfgctx.yaxis_title = "yaxis"
cfgctx.plot_title = "testplot"
cfg = ct.build_pltcfg(cfgctx)
chartcfg = ct.build_cfg(cfg, labels, datavals)



def draw_chart():
    wp = jp.QuasarPage()
    wp.head_html = """<script src = "https://cdn.jsdelivr.net/npm/chart.js" > </script >\n    <link href = "https://unpkg.com/tailwindcss/dist/tailwind.min.css" rel = "stylesheet" >"""

    panel_pltcanvas_ = cj.ChartJS_("panel_canvas", pcp=[], options=chartcfg)
    dbref_canvas = panel_pltcanvas_(wp, "")


    def change_plt(dbref, msg):
        print ("in chage_plt")
        print ("in chage_plt", dbref)
        print ("in chage_plt", msg.page)
        #dbref_canvas.cjsbc.new_chart(msg.page, my_chart_def2)
        #dbref_canvas.cjsbc.new_chart(my_chart_def2)
        dbref_canvas.cjsbc.set_cfgattr("type", "bar")
        dbref_canvas.cjsbc.set_cfgattr("options/scales/y/title/text", "bar")
        
        #await msg.page.update()
        pass
    dbref_btn = dur.button_du("abtn", "abtn", "abtn", change_plt)(wp, "")
    
    return wp


app = jp.app
jp.justpy(draw_chart, start_server=False)


