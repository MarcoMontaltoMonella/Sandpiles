import random, time
from src.constants import MODULUS
from src.tile import Tile
from src.utility import print_space
from colorama import Fore, Back, Style


class Board:
    def __init__(self):
        self.X_SIZE = 4
        self.Y_SIZE = 4
        self.cells = [[Tile(random.randrange(MODULUS), x= x, y= y)
                       for x in range(self.X_SIZE)]
                      for y in range(self.Y_SIZE)]

    def print_board(self):
        time.sleep(0)
        print_space()
        for y in range(self.Y_SIZE):
            for x in range(self.X_SIZE):
                if self.cells[x][y].tapped:
                    print(Fore.RED, end="")
                    self.cells[x][y].tapped = False
                else:
                    print(Fore.GREEN, end="")
                print(self.cells[x][y], end=" ")
                print(Style.RESET_ALL, end="")
            print()

    def tap(self, x, y):
        self.cells[y][x].tapped = True
        self.cells[y][x].inc_by(1)
        if self.cells[y][x].has_to_topple():
            self.topple(self.cells[y][x])
        # TODO: Check why works when x and y are swapped

    def adjacent_tiles(self, tile):
        x, y = tile.x, tile.y
        adj_tiles = []
        if self.cells[x+1][y]:
            adj_tiles.append(self.cells[x+1][y])
        if self.cells[x-1][y]:
            adj_tiles.append(self.cells[x-1][y])
        if self.cells[x][y+1]:
            adj_tiles.append(self.cells[x][y+1])
        if self.cells[x][y-1]:
            adj_tiles.append(self.cells[x][y-1])
        return adj_tiles

    def topple(self, tile):
        tile.val %= MODULUS
        topple_chain = False
        for adj in self.adjacent_tiles(tile):
            adj.inc_by(1)
            if adj.has_to_topple():
                topple_chain = True
        while topple_chain:
            for tile in self.cells:
                if tile.has_to_topple():
                    self.topple(tile)
                    # TODO: Fix has_to_topple called on obj Tile