import random, time
from src.constants import MODULUS
from src.tile import Tile
from src.utility import print_space
from colorama import Fore, Back, Style


class Board:
    def __init__(self):
        self.X_SIZE = 4
        self.Y_SIZE = 4
        self.cells = [[Tile(random.randrange(MODULUS))
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
        # TODO: Check why works when x and y are swapped