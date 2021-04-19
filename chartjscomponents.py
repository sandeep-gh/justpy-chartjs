import demjson
from addict import Dict
from justpy import JustpyBaseComponent
from justpy import WebPage


class ChartJS(JustpyBaseComponent):
    vue_type = 'chartjs'
    # chart_types = [] #TODO

    def __init__(self, **kwargs):
        self.options = Dict()
        self.classes = ''
        self.style = ''
        self.width = 400
        self.height = 200
        self.clear = False
        self.show = True
        self.event_propagation = True
        kwargs['temp'] = False
        super().__init__(**kwargs)
        for k, v in kwargs.items():
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

    async def chart_update(self, update_dict, websocket):
        # https://api.highcharts.com/class-reference/Highcharts.Chart#update
        await websocket.send_json({'type': 'chart_update', 'data': update_dict, 'id': self.id})
        # So the page itself does not update, only the tooltip, return True not None
        return True

    def add_to_page(self, wp: WebPage):
        wp.add_component(self)

    def add_to(self, *args):
        for c in args:
            c.add_component(self)

    def react(self, data):
        pass

    def load_json(self, options_string):
        self.options = Dict(demjson.decode(
            options_string.encode("ascii", "ignore")))
        return self.options

    def load_json_from_file(self, file_name):
        with open(file_name, 'r') as f:
            self.options = Dict(demjson.decode(
                f.read().encode("ascii", "ignore")))
        return self.options

    def convert_object_to_dict(self):

        d = {}
        d['vue_type'] = self.vue_type
        d['id'] = self.id
        d['show'] = self.show
        d['classes'] = self.classes
        d['style'] = self.style
        d['event_propagation'] = self.event_propagation
        d['def'] = self.options
        d['events'] = self.events
        d['width'] = self.width
        d['height'] = self.height
        d['clear'] = self.clear
        d['options'] = self.options

        return d
