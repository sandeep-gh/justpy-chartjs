# td_cjdsl : test drive chartjs dsl
import chartjscomponents as cj
import justpy as jp
import json


my_chart_def = """{
              type: 'bar',
              data: {
                  labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
                  datasets: []
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
    wp = jp.WebPage(classes="h-screen")
    wp.head_html = """<script src = "https://cdn.jsdelivr.net/npm/chart.js" > </script >\n    <link href = "https://unpkg.com/tailwindcss/dist/tailwind.min.css" rel = "stylesheet" >"""

    full_div = jp.Div(a=wp, classes="h-screen  w-screen  bg-pink-100")

    chart_cbox_t = jp.Div(
        a=full_div, classes="bg-green-100  relative  w-1/2 h-1/2")
    chart_cbox_tt = jp.Div(
        a=chart_cbox_t, classes="bg-green-400  relative  w-full h-1/2")
    mychart1 = cj.ChartJS(
        a=chart_cbox_tt, style='background-color: white; border: 1px solid;', classes='m-2', options=my_chart_def)

    chart_cbox_b = jp.Div(
        a=full_div, classes="bg-blue-400 relative w-1/2 h-1/2")

    mychart2 = cj.ChartJS(
        a=chart_cbox_b, style='background-color: white; border: 1px solid;', classes='m-2', options=my_chart_def)
    mychart2.add_dataset(
        """{
        label: "of Votes",
        data: [12, 19, 3, 5, 2, 3],
        backgroundColor: [
                          'rgba(255, 99, 132, 0.2)',
                          'rgba(54, 162, 235, 0.2)',
                          'rgba(255, 206, 86, 0.2)',
                          'rgba(75, 192, 192, 0.2)',
                          'rgba(153, 102, 255, 0.2)',
                          'rgba(255, 159, 64, 0.2)'
                      ],
                      borderColor: [
                          'rgba(255, 99, 132, 1)',
                          'rgba(54, 162, 235, 1)',
                          'rgba(255, 206, 86, 1)',
                          'rgba(75, 192, 192, 1)',
                          'rgba(153, 102, 255, 1)',
                          'rgba(255, 159, 64, 1)'
                      ],
                      borderWidth: 1
                  }""")

    return wp


jp.justpy(draw_chart)
