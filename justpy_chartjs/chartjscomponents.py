import demjson3 as demjson
from addict import Dict
import justpy as jp
from justpy import JustpyBaseComponent
from justpy import WebPage
from tailwind_tags import *
from dpath.util import get as dget, set as dset


def ChartJS_(key, pcp=[], **kwargs):
    def _f(a, tprefix):
        chart_cbox = jp.Div(
            a=a, classes=tstr(bg/green/100, ppos.relative, *pcp))
        _d = ChartJS(key, tprefix, a=chart_cbox,
                     style='background-color: white; border: 1px solid;', **kwargs)
        chart_cbox.ediv = a
        chart_cbox.apk = f'{tprefix}{key}'
        chart_cbox.apkdbmap = Dict()
        chart_cbox.chartjs = _d
        _d.postinit()
        return chart_cbox
    return _f


class ChartJS(JustpyBaseComponent):
    vue_type = 'chartjs'
    # chart_types = [] #TODO

    def __init__(self, key, tprefix,  **kwargs):
        self.options = Dict()
        self.style = ''
        self.classes = ''
        self.width = "0px"
        self.height = "0px"
        self.clear = False
        self.show = True
        self.event_propagation = True
        self.update_create = False
        kwargs['temp'] = False
        self.key = key
        self.id = key

        self.tprefix = tprefix
        super().__init__(**kwargs)
        self.apk = f'{tprefix}{key}'
        self.apkdbmap = Dict()
        for k, v in kwargs.items():
            print("now parsing option ", k, " ", v)
            self.__setattr__(k, v)
        # self.allowed_events = [] #TODO
        for com in ['a', 'add_to']:
            if com in kwargs.keys():
                kwargs[com].add_component(self)

    def __repr__(self):
        return f'{self.__class__.__name__}(id: {self.id}, vue_type: {self.vue_type}, chart options: {self.options})'

    def __setattr__(self, key, value):
        if key == 'options':
            if isinstance(value, str):
                self.load_json(value)
            else:
                self.__dict__[key] = value
        else:
            self.__dict__[key] = value

    def set_title(self, title_text):
        print("opt = ", self.options)
        self.options.options.title.display = True
        self.options.options.title.text = title_text
        print("opt = ", self.options)
        pass

    def set_cfgattr(self, attrpath, attrval):
        dset(self.options, attrpath, attrval)
        print("plt cfg = ", self.options.type)
        self.update_create = True

    def add_dataset(self, dataset_plot_cfg):
        self.options.data.datasets.append(Dict(demjson.decode(
            dataset_plot_cfg.encode("ascii", "ignore"))))
        print("post add dataset =", self.options)

    # async def chart_update(self, update_dict, websocket):
    #     # https://api.highcharts.com/class-reference/Highcharts.Chart#update
    #     await websocket.send_json({'type': 'chart_update', 'data': update_dict, 'id': self.id})
    #     # So the page itself does not update, only the tooltip, return True not None
    #     return True

    def new_chart(self,  new_options):
        self.update_create = True
        self.options = new_options

    def add_to_page(self, wp: WebPage):
        wp.add_component(self)

    def add_to(self, *args):
        for c in args:
            c.add_component(self)

    def react(self, data):
        pass

    def load_json(self, options_string):
        print("load json pre= ", self.options)
        self.options = Dict(demjson.decode(
            options_string.encode("ascii", "ignore")))
        print("load json = ", self.options)
        return self.options

    def load_json_from_file(self, file_name):
        with open(file_name, 'r') as f:
            self.options = Dict(demjson.decode(
                f.read().encode("ascii", "ignore")))
        return self.options

    def postinit(self):
        pass

    def convert_object_to_dict(self):

        d = {}
        d['vue_type'] = self.vue_type
        d['id'] = self.id
        d['show'] = self.show
        d['classes'] = self.classes
        d['style'] = self.style
        d['event_propagation'] = self.event_propagation
        d['def'] = self.options
        print("new chart options = ", d['def'])
        d['events'] = self.events
        d['width'] = self.width
        d['height'] = self.height
        d['clear'] = self.clear
        d['options'] = self.options
        d['update_create'] = self.update_create

        self.update_create = False

        return d
