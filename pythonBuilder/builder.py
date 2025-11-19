class encoding:
   
    def __init__(self):
        self.encoding = {}
        self.currChannel = ""

    def channel(self, channel):
        self.encoding[channel] = {}
        self.currChannel = channel
        return self

    def field(self, name):
        self.encoding[self.currChannel]["field"] = name
        return self


class visualization:

    def __init__(self):
        self.visualization = {"type": "visualization"}

    def mark(self, mark):
        self.visualization["mark"] = mark
        return self

    def add_encoding(self, encoding):
        self.visualization["encoding"] = encoding
        return self



class layout:
    def __init__(self):
        self.layout = {
            "type": "layout",
            "children": [],
        }

    def direction(self, direction):
        self.layout["direction"] = direction
        return self

    def gap(self, gap):
        self.layout["gap"] = gap
        return self
    
    def add_child(self, child):
        self.layout["children"].append(child)
        return self

