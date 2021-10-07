from  jpcjs_tags import *
from  justpy_chartjs import chartjscomponents as cj
#import chartjscomponents as cj
import justpy as jp
import json
import display_components as dc

import tailwind_style_tags as ddt

my_chart_def = """{
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



def draw_chart():
    wp = jp.QuasarPage()
    wp.head_html = """<script src = "https://cdn.jsdelivr.net/npm/chart.js" > </script >\n    <link href = "https://unpkg.com/tailwindcss/dist/tailwind.min.css" rel = "stylesheet" >"""

    panel_pltcanvas_ = cj.ChartJS_("panel_canvas", pcp=[], options=my_chart_def)
    dbref = panel_pltcanvas_(wp, "")
    return wp


app = jp.app
jp.justpy(draw_chart, start_server=False)


