from dpath.util import set as dset
from dpath.util import get as dget
from addict import Dict
from justpy_chartjs.tags import cfg_template as ct
import json
import jsbeautifier

opts = jsbeautifier.default_options()
opts.indent_size = 2

labels = ["ds1", "ds2", "ds3", "ds4", "ds5"]
datavals = [[{'x': 1, 'y': 3}, {'x': 5, 'y': 5}],
            [{'x': 1, 'y': 7}, {'x': 5, 'y': 2}],
            [{'x': 1, 'y': 0}, {'x': 5, 'y': 8}],
            [{'x': 1, 'y': 13}, {'x': 5, 'y': 2}],
            [{'x': 1, 'y': 2}, {'x': 5, 'y': 6}],
            [{'x': 1, 'y': 9}, {'x': 5, 'y': 7}],
            ]


cfgctx = Dict()
cfgctx.plttype = ct.PlotType.Line
cfgctx.xaxis_type = ct.ScaleType.Linear
cfgctx.xaxis_title = "xaxis"
cfgctx.yaxis_title = "yaxis"
cfgctx.plot_title = "testplot"


cfg = ct.build_pltcfg(cfgctx)
newcfg = ct.build_cfg(cfg, labels, datavals)
dset(newcfg, "/options/parsing/xAxisKey",
             "awesomekye")
res = jsbeautifier.beautify(json.dumps(newcfg), opts)
print(res)
