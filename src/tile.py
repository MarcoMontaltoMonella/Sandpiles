from constants import MODULUS

class Tile:
    def __init__(self, val, x, y, target=None, tapped=False):
        self.val = val
        self.target = target
        self.tapped = tapped
        self.x = x
        self.y = y

    def inc_by(self, inc):
        self.val += inc

    def has_to_topple(self):
        return self.val >= MODULUS

    def __str__(self):
        return str(self.val)
