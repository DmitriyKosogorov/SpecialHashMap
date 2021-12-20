from Helpclasses import Index, Forploc, ilocException, plocException

class SpecialHashMap(dict):

    def __init__(self, val=None):
        if val is None:
            val = {}
        super().__init__(val)
        self.changed = False

    def __setitem__(self, item, value):
        super().__setitem__(item, value)
        self.changed = True

    def __delitem__(self, item):
        super().__delitem__(item)
        self.changed = True

    @property
    def iloc(self):
        return Index.iloc(self)

    @property
    def ploc(self):
        return Forploc(self)