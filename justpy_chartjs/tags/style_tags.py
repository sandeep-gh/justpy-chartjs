from .colors import _ColorBase
from aenum import Enum


class Tags:
    title_attr = ("{key}:{val}", "ta", "text", [])


class _twStr:
    def __init__(self, tagstr, arg2):
        self.tagstr = tagstr
        self.arg2 = arg2

    def __truediv__(self, size):
        return self.tagstr.format(val=self.arg2.__truediv__(size))


class TagBase:
    tagstr = None
    tagops = None
    default_key = None

    @classmethod
    def getval(cls, valprefix):
        '''
        tval is tailwind values
        '''

        val = str(valprefix)  # use valprefix if no match is found

        if not cls.tagops:
            return val  # ignore option checking
        for _ in cls.tagops:
            if _.startswith(val):
                val = _
                break
        return val

    @classmethod
    def __truediv__(cls, valprefix):
        if isinstance(valprefix, TagBase):

            return _twStr(cls.tagstr, valprefix)

        if isinstance(valprefix, _ColorBase):

            return _twStr(cls.tagstr, valprefix)

        if isinstance(valprefix, Enum):
            return valprefix.value

        val = cls.getval(valprefix)
        return cls.tagstr.format(key=cls.default_key, val=val)


taglist = [attr for attr in dir(Tags) if not callable(
    getattr(Tags, attr)) and not attr.startswith("__")]


for _ in taglist:
    taginfo = getattr(Tags, _)
    globals()[taginfo[1]] = type(taginfo[1], (TagBase,), {'tagstr': taginfo[0], 'tagops': taginfo[3],
                                                          'default_key': taginfo[2]})()
