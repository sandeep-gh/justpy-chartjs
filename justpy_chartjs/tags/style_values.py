from aenum import Enum

class Position(Enum):
    top = "top"
    left = "left"
    bottom = "bottom"
    right = "right"
    chart = "chartArea"
    pass

class Align(Enum):
    start = "start"
    center = "center"
    end = "end"
    
class PlotType(Enum):
    line = """type:'line'"""
    bar = """type:bar"""
    pass


# options namespace
class MaintainAspectRatio(Enum):
    t = "maintainAspectRatio:true"
    f = "maintainAspectRatio:false"
    pass


class Axis(Enum):
    x = "x"
    y = "y"
    y1 = "y1"

class Color:
    black = "#000000"
    white = "#FFFFFF"
    red =  "#FF0000"
    
