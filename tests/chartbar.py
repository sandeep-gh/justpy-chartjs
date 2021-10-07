

#chartbar shows all kinds of charts

from addict import Dict
import justpy as jp
from tailwind_style_tags import *
from jpcjs_tags import *
from justpy_utils import DivM
import chartjscomponents as cj
import display_units_reversed as dur
import display_components as dc

def chart_type_1(key, pcp=[]):

    data = tld(l=["a", "b", "c"], ldu=[
        du(l="""'sales by year'""", d=[20, 40, 100]),
        du(l="""'purchase by year'""", d=[10, 30, 60]),
    ]
    )
    title = "{" + ",".join([ta/"""'Hello World'""", ta/pos.top]) + "}"
    options = "{" + ",".join([mar.f.value]) + "}"
    cfg = cjstr(pt.line,  tld=data, title=title, options=options)
    print (cfg)
    
    
    def generator(a, tprefix=""):
        chart_cbox = jp.Div(
            a=a, classes=tstr(bg/green/100, ppos.relative, *pcp))
        mychart = cj.ChartJS("achart", tprefix,
            a=chart_cbox,  style='background-color: white; border: 1px solid;', classes='m-2', options=cfg)
        chart_cbox.apk = "achart"
        return chart_cbox

    return generator


def launcher():
    wp = jp.WebPage(classes="h-screen")
    wp.head_html = """<script src = "https://cdn.jsdelivr.net/npm/chart.js" > </script >\n    <link href = "https://unpkg.com/tailwindcss/dist/tailwind.min.css" rel = "stylesheet" >"""


    tlc_ = dc.StackG_("ae_tlc", 4, 6,  cgens=[chart_type_1('myfirst', pcp=[col/span/4, row/span/2])],
                            pcp=[bt.container, mr/x/"auto", H/"screen", bg/gray/4])

    wpcts = tlc_(wp, "")
    return wp



app = jp.app
jp.justpy(launcher, start_server=False)
 
