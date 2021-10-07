class _ColorBase:
    mycolor = None

    @ classmethod
    def __truediv__(cls, colorval):
        return f"{cls.mycolor}-{colorval}00"

    @ classmethod
    def __pow__(cls, colorval):
        return f"{cls.mycolor}-{colorval}00"

    @classmethod
    def __repr__(cls):
        return f"{cls.mycolor}"


blueGray = coolGray = gray = trueGray = warmGray = red = orange = amber = yellow = lime = green = emerald = teal = cyan = lightBlue = blue = indigo = violet = purple = fuchsia = pink = rose = None

_tw_color_list = ["blueGray", "coolGray", "gray", "trueGray", "warmGray", "red", "orange", "amber", "yellow", "lime",
                  "green", "emerald", "teal", "cyan", "lightBlue", "blue", "indigo", "violet", "purple", "fuchsia", "pink", "rose"]

for color in _tw_color_list:
    globals()[color.capitalize()] = type(color.capitalize(), (_ColorBase,),

                                         {'mycolor': color})

    globals()[color] = globals()[color.capitalize()]()
