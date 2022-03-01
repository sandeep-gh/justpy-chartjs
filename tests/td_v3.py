import justpy as jp
from  justpy_chartjs import chartjscomponents as cj

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

              data: {
labels: [0,1,2,3,4, 5, 6, 7],
                  datasets: [
{
data: [65, 59, 80, 81, 56, 55, 40],

label: "obs",
borderColor: 'rgb(75, 192, 192)',
tension: 0.1
}
]
              },
              options: {
                  title: {
                      display: true,
                      text: 'Custom Chart Title',
position: 'bottom'
                  }
              }
          }"""


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
    wp.tailwind = True
    wp.head_html = """<script src = "https://cdn.jsdelivr.net/npm/chart.js" > </script >\n    <link href = "https://unpkg.com/tailwindcss/dist/tailwind.min.css" rel = "stylesheet" >"""

    panel_pltcanvas_ = cj.ChartJS_("panel_canvas", pcp=[], options=my_chart_def)
    dbref = panel_pltcanvas_(wp, "")
    return wp


app = jp.app
jp.justpy(draw_chart, start_server=False)


