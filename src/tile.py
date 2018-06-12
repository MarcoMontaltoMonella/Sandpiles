class Tile:
    def __init__(self, val, target=None, tapped=False):
        self.val = val
        self.target = target
        self.tapped = tapped

    def inc_by(self, inc):
        self.val += inc

    def __str__(self):
        return str(self.val)
