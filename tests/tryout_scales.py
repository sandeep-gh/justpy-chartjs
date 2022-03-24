from versa_engine.common.plot_utils import pick_colors_from_anchors
from addict import Dict

colorSchemes = {"default": ["#7f3b08", "#f7f7f7", "#2d004b"]
                }

colorset = default_colorset = pick_colors_from_anchors(
    colorSchemes["default"], 8)

labels = ["ds1", "ds2", "ds3", "ds4", "ds5"]
datavals = [[{'x': 1, 'y': 3}, {'x': 5, 'y': 5}, {'x': 7, 'y': 7}],
            [{'x': 1, 'y': 7}, {'x': 5, 'y': 2}, {'x': 7, 'y': 3}],
            [{'x': 1, 'y': 0}, {'x': 5, 'y': 8}, {'x': 7, 'y': 5}],
            [{'x': 1, 'y': 13}, {'x': 5, 'y': 2}, {'x': 7, 'y': 1}],
            [{'x': 1, 'y': 2}, {'x': 5, 'y': 6}, {'x': 7, 'y': 6}],
            [{'x': 1, 'y': 9}, {'x': 5, 'y': 7}, {'x': 7, 'y': 9}],
            ]


def datagen(labels, datavals):
    for idx, label, dataval in zip(range(len(labels)), labels, datavals):
        dataitem = Dict(track_changes=True)
        dataitem.label = label
        dataitem.data = dataval
        dataitem.borderColor = colorset[idx]
        dataitem.backgroundColor = colorset[idx]
        yield dataitem


def add_dataset(chartcfg):
    """add plotting to chartcfg
    """

    chartcfg.data.datasets = [_ for _ in datagen(labels, datavals)]
