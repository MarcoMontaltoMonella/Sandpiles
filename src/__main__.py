from src.board import *
from random import randrange
from colorama import Fore, Back, Style


def main():
    board = Board()
    board.print_board()
    tap_x, tap_y = randrange(board.X_SIZE), randrange(board.Y_SIZE)
    print("\nAbout to tap: "+ Fore.RED + "(" + str(tap_x) + ", " + str(tap_y) + ")" + Style.RESET_ALL)
    board.tap(tap_x, tap_y)
    board.print_board()

if __name__ == '__main__':
    main()
