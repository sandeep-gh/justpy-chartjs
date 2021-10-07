#from style_values import TitlePosition as ttp
from .style_tags import *
from .style_values import Position as pos, PlotType as pt, MaintainAspectRatio as mar
from addict import Dict


def du(**kwargs):
    '''
    a data unit; in chartjs term its the label, data pair -- the data whose values gets plotted on the chart
    '''
    ans = ""
    dd = Dict(kwargs)
    ans += f"label:{dd.l},"
    ans += f"data:{dd.d}"
    return '{' + ans + "}"


def tld(**kwargs):
    '''
    top level data;
    in chartjs term its the data block consisting
    of label and dataset
    '''
    ans = ""
    dd = Dict(kwargs)
    ans += f"labels:{dd.l},"
    ans += "datasets:[" + ",".join(dd.ldu) + "]"
    return "{" + ans + "}"


def cjstr(*args, **kwargs):
    cfg = ""
    l = []
    for arg in args:  # simplify this
        if isinstance(arg, Enum):
            l.append(arg.value)
    cfg += ",".join(l)

    dd = Dict(kwargs)
    cfg += ", data:" + dd.tld
    cfg += "," + "title:" + dd.title
    cfg += "," + "options:" + dd.options

    return "{" + cfg + "}"
