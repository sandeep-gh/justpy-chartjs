import justpy as jp


def draw_chart():
    wp = jp.WebPage()
    wp.head_html = '<link href="https://unpkg.com/tailwindcss/dist/tailwind.min.css" rel="stylesheet">'
    full_div = jp.Div(
        a=wp, classes="w-screen h-screen bg-pink-100")

    tt = jp.Div(a=full_div, classes="w-1/2 h-1/2 bg-gray-400")
    jp.P(a=tt, text="area1")

    #jp.Div(a=full_div, classes="h-8  bg-gray-200", text="2")
    return wp


jp.justpy(draw_chart)
