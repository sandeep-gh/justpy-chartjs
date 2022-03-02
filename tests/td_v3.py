import justpy as jp
from justpy_chartjs import chartjscomponents as cj

# my_chart_def = """{
#               type: 'bar',
#               data: {
#                   labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
#                   datasets: [{
# data: [5,6,7,8,9,10, 11]

# }
# ]
#               },
#               options: {
#                   scales: {
#                       y: {
#                           beginAtZero: true
#                       }
#                   },

#                   title: {
#                       display: true,
#                       text: 'Custom Chart Title',
# position: 'bottom'
#                   }
#               }
#           }"""

my_chart_def = """{
              type: 'line',
              data: {
                  labels: [5,6,7,8,9,10, 11],
                  datasets: [{
data: [5,6,7,8,9,10, 11]

}
]
              },
              options: {
                  scales: {
                      y: {
                          beginAtZero: true
                      },
                      x: { 
                          grid: {
display: false 
}
}
                  },


                  title: {
                      display: true,
                      text: 'Custom Chart Title',
position: 'bottom'
                  }
              }
          }"""

my_chart_def = """
{"type": "line", "options": {"responsive": true, "aspectRatio": 2, "resizeDelay": 4, "devicePixelRatio": 1, "parsing": false, "plugins": {"legend": {"position": "top"}, "title": {"display": true, "text": "plot_title"}}, "elements": {"line": {"tension": 0, "backgroundColor": null, "borderWidth": 2, "borderColor": null, "capBezierPoints": true}}, "scales": {"xAxis": {"grid": {"display": true}}}}, "data": {"datasets": [{"label": "ds1", "data": [{"x": 1, "y": 3}, {"x": 5, "y": 5}], "borderColor": "#7f3b08", "backgroundColor": "#7f3b08"}, {"label": "ds2", "data": [{"x": 1, "y": 7}, {"x": 5, "y": 2}], "borderColor": "#996742", "backgroundColor": "#996742"}, {"label": "ds3", "data": [{"x": 1, "y": 0}, {"x": 5, "y": 8}], "borderColor": "#a7826e", "backgroundColor": "#a7826e"}, {"label": "ds4", "data": [{"x": 1, "y": 13}, {"x": 5, "y": 2}], "borderColor": "#a98b87", "backgroundColor": "#a98b87"}, {"label": "ds5", "data": [{"x": 1, "y": 2}, {"x": 5, "y": 6}], "borderColor": "#9d8291", "backgroundColor": "#9d8291"}], "labels": "[1,2,4,5]"}}
"""


def draw_chart():
    wp = jp.QuasarPage()
    # <script src = "https://cdnjs.cloudflare.com/ajax/libs/Chart.js/3.7.1/chart.js"></script >\n
    wp.head_html = """

    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

    <script src="https://cdn.tailwindcss.com/"></script>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/inter-ui@3.13.1/inter.min.css">
    """
    wp.css = 'body { font-family: Inter; }'
    wp.tailwind = False
    #wp.head_html = """<script src = "https://cdn.jsdelivr.net/npm/chart.js" > </script >\n    <link href = "https://unpkg.com/tailwindcss/dist/tailwind.min.css" rel = "stylesheet" >"""

    panel_pltcanvas_ = cj.ChartJS_(
        "panel_canvas", pcp=[], options=my_chart_def)
    dbref = panel_pltcanvas_(wp, "")
    return wp


app = jp.app
jp.justpy(draw_chart, start_server=False)
