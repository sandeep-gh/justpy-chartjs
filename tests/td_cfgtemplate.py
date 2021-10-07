from addict import Dict
import jpcjs_tags.cfg_template as ct
import common.plot_utils as plu
import json
import jsbeautifier

opts = jsbeautifier.default_options()
opts.indent_size = 2

labels = ["ds1", "ds2", "ds3", "ds4", "ds5"]
datavals = [ [{'x': 1, 'y':3}, {'x':5, 'y':5}],
             [{'x': 1, 'y':7}, {'x':5, 'y':2}],
             [{'x': 1, 'y':0}, {'x':5, 'y':8}],
             [{'x': 1, 'y':13}, {'x':5, 'y':2}],
             [{'x': 1, 'y':2}, {'x':5, 'y':6}],
             [{'x': 1, 'y':9}, {'x':5, 'y':7}],
    ]
anchors = ['#66FF66', '#660066', '#993333']
colors = plu.pick_colors_from_anchors(anchors, len(datavals))
cfgctx = Dict()
cfgctx.plttype = ct.PlotType.Line
cfgctx.xaxis_type = ct.ScaleType.Linear
cfgctx.xaxis_title = "xaxis"
cfgctx.yaxis_title = "yaxis"
cfgctx.plot_title = "testplot"

newcfg = ct.build_cfg(cfgctx, labels, datavals)
res = jsbeautifier.beautify(json.dumps(newcfg), opts)
print(res)

