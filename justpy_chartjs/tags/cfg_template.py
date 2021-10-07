from addict import Dict
from .style_values import Align, Position
from .style_values import Axis
from typing import NamedTuple, Any
from aenum import Enum, auto
from common.plot_utils import pick_colors_from_anchors
#Chart.defaults.datasets.line.showLine = false;


colorSchemes = { "default" : ["#7f3b08", "#f7f7f7", "#2d004b"  ]
    }

colorset = default_colorset = pick_colors_from_anchors(colorSchemes["default"], 25)

class TextColor(Enum):
    pass

class BackgroundColor(Enum):
    pass

class BorderColor(Enum):
    pass
textcolor = "#000000"
backgroundcolor = "#fee0b6"

print (default_colorset)
class PointStyle(Enum):
    circle = "circle"
    cross = "cross"
    crossRot = "crossRot"
    dash = "dash"
    line = "line"
    rect = "rect"
    rectRounded = "rectRounded"
    star = "star"
    triangle = "triangle"

class ScaleType(Enum):
    Linear = "linear"
    Logarithmic = "logarithmic"
    Category = "category"
    Time = "time"
    Timeseries = "timeseries"

#config parameter types
class CPT(Enum): 
    simple = "simple"
    simplemore = "simplemore"
    nitpick = "nitpick"
    ocd = "ocd"
    perf = "perf"
    config = "config"
    advanced = "advanced"
    required = "required"
    TBD = "tbd"
    ninja = "ninja"

class CfgattrMeta(NamedTuple):
    default : Any
    vtype : Any
    vrange : Any 
    decor_type: Any
    
class Color(Enum):
    pass 
class PlotType(Enum):
    Line  = "line"
    Bar = "bar"
    Scatter = "scatter"
    Bubble = "bubble"
# def set_scale_attr(sdict):
#     #sdict.stacked = False
#     #sdict.type = None #tree shake it; decor param
#     sdict.display = True
#     sdict.grid = Dict()
#     sdict.grid.drawonChartArea = False
#     sdict.title = Dict()
#     sdict.title.display = True
#     sdict.title.text = "" #required parameter
#     sdict.title.align = Align.center.value
#     sdict.title.font = Dict()
#     sdict.title.font.family = 'Times'
#     sdict.title.font.size = 5
#     sdict.title.font.style = 'normal'
#     sdict.title.font.lineHeight = 1.2
#     sdict.padding = Dict() #decor param: should be opened upon click.
#     sdict.padding.top = 5
#     sdict.padding.left = 2
#     sdict.padding.right = 2
#     sdict.padding.bottom = 2
#     #sdict.min = None #treeshake
#     #sdict.max = None #treeshake


def datagen(labels, datavals):
    for idx, label, dataval in zip(range(len(labels)), labels, datavals):
        dataitem = Dict()
        dataitem.label = label
        dataitem.data = dataval
        dataitem.borderColor = colorset[idx]
        dataitem.backgroundColor = colorset[idx]
        #dataitem.stack = None #treeshake it; defines a group
        #dataitem.borderWidth = 2 #decor parameter
        #dataitem.borderRadius = 5 #decor parameter
        #dataitem.borderDash = [3, 3] #decor param
        #dataitem.yAxisID = 'y' #config param
        #dataitem.fill = False #decor param
        # if pltctx.plttype in ['line']:
        #     dataitem.cubicInterpolationModel = 'cubic' #decor param
        #     dataitem.tension = 0.5
        yield dataitem



def build_pltcfg(cfgctx):

    cfg = Dict()
    cfg.type = CfgattrMeta(PlotType.Line, PlotType, PlotType, CPT.simple)

    cfg.options = Dict()
    cfg.options.responsive = CfgattrMeta(True, bool, bool, CPT.config)
    cfg.options.maintainAspectRatio = CfgattrMeta(False, bool, bool, CPT.advanced)
    cfg.options.aspectRatio = CfgattrMeta(2, int, [1, 4], CPT.simplemore)
    cfg.options.resizeDelay = CfgattrMeta(4, int, [0, 10], CPT.advanced)

    cfg.options.devicePixelRatio = CfgattrMeta(1, int, [0, 10], CPT.advanced)
    cfg.options.parsing = CfgattrMeta(False, bool, bool, CPT.advanced)
    cfg.options.interaction = Dict()

    cfg.options.interaction.mode = CfgattrMeta("nearest", str, ['point', 'nearest', 'index', 'bar', 'dataset', 'x', 'y'], CPT.advanced)

    cfg.options.interaction.intersect = CfgattrMeta(True, bool, bool, CPT.advanced)
    cfg.options.interaction.axis = CfgattrMeta('x', str, ['x', 'y', 'xy'], CPT.ninja)

    #TBD events : https://www.chartjs.org/docs/latest/configuration/interactions.html
    #TBD: https://www.chartjs.org/docs/latest/configuration/interactions.html#converting-events-to-data-values

    cfg.options.indexAxis = CfgattrMeta(None, None, None, CPT.TBD) #Axis.x.value
    cfg.options.plugins = Dict()
    cfg.options.plugins.legend = Dict()
    cfg.options.plugins.legend.position = CfgattrMeta(Position.top, Position, Position, CPT.simplemore)

    cfg.options.plugins.title = Dict()
    cfg.options.plugins.title.display = CfgattrMeta(True, bool, bool, CPT.simplemore)
    cfg.options.plugins.title.text = CfgattrMeta(cfgctx["plot_title"], str, str, CPT.simple) 
    cfg.options.elements = Dict()

    #configure point ui-elem look-and-feel
    if cfgctx.plttype in [PlotType.Line, PlotType.Bubble]:
        _ = cfg.options.elements.point = Dict()
        _ = cfg.options.elements.point
        _.radius = CfgattrMeta(3, int, [0,5], CPT.nitpick)
        _.pointStyle = CfgattrMeta(PointStyle.circle, PointStyle, PointStyle, CPT.nitpick)
        _.backgroundColor = CfgattrMeta("", Color, BackgroundColor, CPT.simplemore)
        _.borderWidth = CfgattrMeta(2, int, [0,5], CPT.nitpick)
        _.borderColor =  CfgattrMeta("", Color, BorderColor, CPT.nitpick)
        _.hitRadius = CfgattrMeta(1, int, [0, 3], CPT.TBD)
        _.hoverRadius = CfgattrMeta(2, int, [0,5], CPT.TBD)
        _.hoverBorderWidth = CfgattrMeta(1, int, [0,5], CPT.TBD)

    
    if cfgctx.plttype in [PlotType.Line]:
        _ = cfg.options.elements.line = Dict()
        _.tension = CfgattrMeta(0, float, [0,1], CPT.advanced)
        _.backgroundColor = CfgattrMeta("", Color, BackgroundColor, CPT.simplemore)
        _.borderWidth = CfgattrMeta(2, int, [0,5], CPT.nitpick)
        _.borderColor =  CfgattrMeta("", Color, BorderColor, CPT.simplemore)
        _.borderCapStyle =  CfgattrMeta("butt", None, None, CPT.TBD)
        _.borderDash = CfgattrMeta([], None, None, CPT.TBD)
        _.borderDashOffset = CfgattrMeta(0.0, None, None, CPT.TBD)
        _.borderJoinStyle = CfgattrMeta("miter", None, None, CPT.TBD)
        _.capBezierPoints = CfgattrMeta(True, bool, bool, CPT.advanced)
        _.cubicInterpolationMode = CfgattrMeta("default", None, None, CPT.TBD)
        _.fill = CfgattrMeta(None, None, None, CPT.TBD)
        _.stepped = CfgattrMeta(None, None, None, CPT.TBD)

        if cfgctx.xaxis_type in [ScaleType.Linear, ScaleType.Time] and cfgctx.parsing == False:
            _ = cfg.options.plugins.decimation = Dict()
            _.enabled = CfgattrMeta(False, bool, bool, CPT.advanced)
            _.algorithm = CfgattrMeta('min-max', str, ['min-max', 'lttb'], CPT.advanced)
            _.samples = CfgattrMeta(None, int, int, CPT.TBD)
            _.threshold = CfgattrMeta(None, int, int, CPT.TBD)

    if cfgctx.plttype in [PlotType.Bar]:
        cfg.options.elements.bar = Dict()
        _ = cfg.options.elements.bar
        _.backgroundColor = CfgattrMeta("", Color, BackgroundColor, CPT.simple)
        _.borderWidth = CfgattrMeta(2, int, [0,5], CPT.nitpick)
        _.borderColor = CfgattrMeta("", Color, BorderColor, CPT.nitpick)
        _.borderSkipped = CfgattrMeta('start', str, ['bottom', 'left', 'top', 'right', 'false'], CPT.advanced)
        _.borderRadius =  CfgattrMeta( 2, int, [0,6], CPT.nitpick)
        _.pointStyle = CfgattrMeta( 'circle', PointStyle, PointStyle, CPT.nitpick)

        
    #configure scales     
    if cfgctx.plttype in [PlotType.Bar, PlotType.Line]:
        cfg.options.scales = Dict()
        _ = cfg.options.scales.xAxis = Dict()
        _.type = CfgattrMeta('linear', ScaleType, ScaleType, CPT.advanced)
        _.alignToPixels = CfgattrMeta(False, bool, bool, CPT.TBD)
        _.backgroundColor = CfgattrMeta("", Color, BackgroundColor, CPT.simple)
        #TBD: padding
        _.min = CfgattrMeta(None, int, int, CPT.config)
        _.max = CfgattrMeta(None, int, int, CPT.config)
        _.reversed = CfgattrMeta(False, bool, bool, CPT.TBD)
        _.stacked = CfgattrMeta(False, bool, bool, CPT.config) # should the data be scaled
        _.suggestedMax = CfgattrMeta(None, int, int, CPT.TBD)
        _.suggestedMin = CfgattrMeta(None, int, int, CPT.TBD)
        _.weight = CfgattrMeta(0, int, int, CPT.TBD) #move away from chart area
        _.ticks = Dict() #TBD
        _.ticks.backdropColor = CfgattrMeta("", Color, Color, CPT.nitpick) #background color for label
        _.ticks.backdropPadding = CfgattrMeta(2, int, [0,5], CPT.advanced) #padding for label backdrop
        _.ticks.callback = CfgattrMeta(None, None, None, CPT.TBD)
        _.ticks.display = CfgattrMeta(True, bool, bool, CPT.simple)
        _.ticks.color = CfgattrMeta("", Color, Color, CPT.nitpick) #TBD
        _.ticks.font = CfgattrMeta(None, None, None, CPT.TBD)
        #_.ticks.major = Dict() #TBD: major tick formatting
        _.ticks.padding = CfgattrMeta(2, int, int, CPT.nitpick)
        _.ticks.showLabelBackdrop = CfgattrMeta(False, bool, bool, CPT.nitpick)
        _.ticks.textStrokeColor = CfgattrMeta("", Color, Color, CPT.TBD)
        _.ticks.textStrokeWidth = CfgattrMeta(0, int, int, CPT.TBD)

        _.ticks.z = CfgattrMeta(0, int, int, CPT.advanced)
        _.ticks.align = CfgattrMeta('center', ['start', 'center', 'end'], ['start', 'center', 'end'], CPT.ocd)
        _.ticks.crossAlign = CfgattrMeta("near", ["near", "center", "far"], ["near", "center", "far"], CPT.ocd)
        _.ticks.sampleSize = CfgattrMeta(None, None, None, CPT.TBD)
        _.ticks.autoSkip = CfgattrMeta(True, bool, bool, CPT.advanced)
        _.ticks.autoSkipPadding = CfgattrMeta(3, int, int, CPT.advanced)
        _.ticks.includeBounds = CfgattrMeta(None, None, None, CPT.TBD)
        _.ticks.labelOffset = CfgattrMeta(0, int, [0,5], CPT.nitpick)
        _.ticks.maxRotation = CfgattrMeta(50, int, [0, 100], CPT.advanced)
        _.ticks.minRotation = CfgattrMeta(0, int, [0,100], CPT.simple)
        _.ticks.mirror = CfgattrMeta(False, bool, bool, CPT.advanced)

        _.grid = Dict() #TBD
        _.grid.display = CfgattrMeta(False, bool, bool, CPT.simplemore)
        _.grid.color = CfgattrMeta("", Color, Color, CPT.simple)
        _.grid.borderColor = CfgattrMeta("", Color, Color, CPT.nitpick)
        _.grid.tickColor = CfgattrMeta("", Color, Color, CPT.nitpick)
        _.grid.circular = CfgattrMeta(None, None, None, CPT.TBD) #from for radar chart
        
        #TBD: other grid parameters
        #https://www.chartjs.org/docs/2.9.4/axes/styling.html?h=grid
        
        _.title = Dict()
        _.title.color = CfgattrMeta("", Color, TextColor, CPT.nitpick)
        _.title.display = CfgattrMeta(True, bool, bool, CPT.simplemore)
        _.title.text = CfgattrMeta(cfgctx["xaxis_title"], str, str, CPT.simple)    

        #The yAxis
        cfg.options.scales.yAxis = Dict()
        _ = cfg.options.scales.yAxis
        _.type = CfgattrMeta('linear', ScaleType, ScaleType, CPT.advanced) #TBD this doesn't need to be linear
        _.alignToPixels = CfgattrMeta(False, bool, bool, CPT.TBD)
        _.backgroundColor = CfgattrMeta("", Color, BackgroundColor, CPT.simple)

        _.min = CfgattrMeta(None, int, int, CPT.config)
        _.max = CfgattrMeta(None, int, int, CPT.config)
        _.reversed = CfgattrMeta(False, bool, bool, CPT.TBD)
        _.stacked = CfgattrMeta(False, bool, bool, CPT.config) # should the data be scaled
        _.suggestedMax = CfgattrMeta(None, int, int, CPT.TBD)
        _.suggestedMin = CfgattrMeta(None, int, int, CPT.TBD)
        _.weight = CfgattrMeta(0, int, int, CPT.TBD) #move away from chart area
        _.ticks = Dict() #TBD
        _.ticks.backdropColor = CfgattrMeta("", Color, BackgroundColor, CPT.nitpick) #background color for label
        _.ticks.backdropPadding = CfgattrMeta(2, int, [0,5], CPT.advanced) #padding for label backdrop
        _.ticks.callback = CfgattrMeta(None, None, None, CPT.TBD)
        _.ticks.display = CfgattrMeta(True, bool, bool, CPT.simple)
        _.ticks.color = CfgattrMeta("", Color, Color, CPT.nitpick)
        _.ticks.font = CfgattrMeta(None, None, None, CPT.TBD)
        #_.ticks.major = Dict() #TBD: major tick formatting
        _.ticks.padding = CfgattrMeta(2, int, int, CPT.nitpick)
        _.ticks.showLabelBackdrop = CfgattrMeta(False, bool, bool, CPT.nitpick)
        _.ticks.textStrokeColor = CfgattrMeta("", Color, Color, CPT.TBD)
        _.ticks.textStrokeWidth = CfgattrMeta(0, int, int, CPT.TBD)

        _.ticks.z = CfgattrMeta(0, int, int, CPT.advanced)
        _.ticks.align = CfgattrMeta('center', ['start', 'center', 'end'], ['start', 'center', 'end'], CPT.ocd)
        _.ticks.crossAlign = CfgattrMeta("near", ["near", "center", "far"], ["near", "center", "far"], CPT.ocd)
        _.ticks.sampleSize = CfgattrMeta(None, None, None, CPT.TBD)
        _.ticks.autoSkip = CfgattrMeta(True, bool, bool, CPT.advanced)
        _.ticks.autoSkipPadding = CfgattrMeta(3, int, int, CPT.advanced)
        _.ticks.includeBounds = CfgattrMeta(None, None, None, CPT.TBD)
        _.ticks.labelOffset = CfgattrMeta(0, int, [0,5], CPT.nitpick)
        _.ticks.maxRotation = CfgattrMeta(50, int, [0, 100], CPT.advanced)
        _.ticks.minRotation = CfgattrMeta(0, int, [0,100], CPT.simple)
        _.ticks.mirror = CfgattrMeta(False, bool, bool, CPT.advanced)

        _.grid = Dict() #TBD
        _.grid.display = CfgattrMeta(False, bool, bool, CPT.simplemore)
        _.grid.color = CfgattrMeta("", Color, Color, CPT.simple)
        _.grid.borderColor = CfgattrMeta("", Color, Color, CPT.nitpick)
        _.grid.tickColor = CfgattrMeta("", Color, Color, CPT.nitpick)
        _.grid.circular = CfgattrMeta(None, None, None, CPT.TBD) #from for radar chart
        
        #TBD: other grid parameters
        #https://www.chartjs.org/docs/2.9.4/axes/styling.html?h=grid
        
        _.title = Dict()
        _.title.color = CfgattrMeta("", Color, Color, CPT.nitpick)
        _.title.display = CfgattrMeta(True, bool, bool, CPT.simplemore)
        _.title.text = CfgattrMeta(cfgctx["yaxis_title"], str, str, CPT.simple)
        
    return cfg
#[set_scale_attr(v) for k, v in cfg.options.scales.items()]

def cfgattreval(key, cam, colorbank):
    '''
    cam: CfgattrMeta
    '''
    if not isinstance(cam, CfgattrMeta):
        print (key, cam)
        
    if cam.decor_type == CPT.TBD or cam.decor_type == None:
        return None
    if cam.default == "":

        if cam.vtype == Color:
            if cam.vtype == BackgroundColor:
                return backgroundcolor
            if cam.vtype == TextColor:
                return textcolor
            if cam.vtype == BorderColor:
                return backgroundcolor
            return  next(colorbank)

        return None#these are required
    if isinstance(cam.default, Enum):
        return cam.default.value
    return cam.default
    
        

def walker(adict, ppath=""):
    for key, value in adict.items():
        #print ("key = ", key)
        if isinstance(value, Dict):
            #print (value)
            yield from walker(value, ppath + f"/{key}")
        else:
            yield (f"{ppath}/{key}", value)                   #cfgattreval(f"{ppath}/{key}", value)
            pass

            


#def build_cfg(cfgctx, dataiter, plot_type, plot_title, xtitle, ytitle):

def build_cfg(cfg, labels, datavals):
    newcfg = Dict()
    def xwalker(adict, newd, colorbank):
        for key, value in adict.items():
            #print ("key = ", key)
            if isinstance(value, Dict):
                #print (value)
                x = Dict()
                setattr(newd, key, x)
                xwalker(value, x, colorbank)
            else:
                evalue = cfgattreval(key, value, colorbank)
                if evalue is not None:
                    setattr(newd, key, evalue)
                pass

    xwalker(cfg, newcfg, iter(colorset))
    newcfg.data.datasets = [_ for _ in datagen(labels, datavals)]
    return newcfg
    

 
