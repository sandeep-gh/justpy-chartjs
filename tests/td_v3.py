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

# data: [0.90, 0.89, 0.88, 0.88, 0.89, 0.90, 0.89, 0.89, 0.87, 0.88, 0.86, 0.83,
#          0.80, 0.77, 0.76, 0.82, 0.79, 0.82, 0.83, 0.82, 0.84, 0.82, 0.86, 0.89,
#          0.87, 0.90, 0.88, 0.87, 0.89, 0.90, 0.84, 0.87, 0.85, 0.81, 0.76, 0.74,
#          0.77, 0.79, 0.75, 0.69, 0.69, 0.69, 0.72, 0.72, 0.76, 0.78, 0.78, 0.82,
#          0.85, 0.85, 0.83, 0.86, 0.85, 0.86, 0.84, 0.82, 0.82, 0.81, 0.78, 0.75,
#          0.77, 0.73, 0.75, 0.73, 0.75, 0.77, 0.77, 0.76, 0.77, 0.79, 0.79, 0.79,
#          0.81, 0.85, 0.84, 0.87, 0.86, 0.82, 0.82, 0.83, 0.81, 0.79, 0.79, 0.76,
#          0.79, 0.75, 0.77, 0.80, 0.80, 0.83, 0.84, 0.85, 0.85, 0.84, 0.84, 0.84,
#          0.88, 0.86, 0.85, 0.86, 0.86, 0.86, 0.85, 0.84, 0.73, 0.62, 0.66, 0.58,
#          0.52, 0.45, 0.42, 0.39, 0.40, 0.42, 0.48, 0.52, 0.56, 0.52, 0.49, 0.49,
#          0.45, 0.47, 0.53, 0.48, 0.44, 0.42, 0.42, 0.42, 0.38, 0.32, 0.34, 0.31,
#          0.30, 0.30, 0.30, 0.29, 0.34, 0.32, 0.33, 0.35, 0.36, 0.37, 0.38, 0.38,
#          0.38, 0.45, 0.40, 0.37, 0.39, 0.38, 0.33, 0.31, 0.33, 0.39, 0.47, 0.43,
#          0.41, 0.43, 0.43, 0.43, 0.45, 0.46, 0.49, 0.52, 0.55, 0.60, 0.59, 0.65,
#          0.64, 0.64, 0.61, 0.62, 0.55, 0.54, 0.54, 0.56, 0.53, 0.59, 0.63, 0.68,
#          0.69, 0.68, 0.74, 0.72, 0.71, 0.68, 0.70, 0.69, 0.73, 0.72, 0.72, 0.73,
#          0.76, 0.71, 0.76, 0.69, 0.65, 0.64, 0.68],

my_chart_def = """{
              type: 'line',
<<<<<<< HEAD
              data: {
                  labels: [5,6,7,8,9,10, 11],
                  datasets: [{
data: [5,6,7,8,9,10, 11]
=======

              data: {
labels: [0,1,2,3,4, 5, 6, 7],
                  datasets: [
{
data: [65, 59, 80, 81, 56, 55, 40],
>>>>>>> 08170d4ef2bb951c39394d0831eca5bea8f3bf97

label: "obs",
borderColor: 'rgb(75, 192, 192)',
tension: 0.1
}
]
              },
              options: {
<<<<<<< HEAD
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


=======
>>>>>>> 08170d4ef2bb951c39394d0831eca5bea8f3bf97
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
    panel_pltcanvas_ = cj.ChartJS_(
        "panel_canvas", pcp=[], options=my_chart_def)
    dbref = panel_pltcanvas_(wp, "")
    return wp


app = jp.app
jp.justpy(draw_chart, start_server=False)
