import os
import numpy as np


class Board:
    def __init__(self, board_data):
        self.data = np.array([data.split() for data in board_data], ndmin=2)
        self.virtual_data = self.data.copy()

    def mark(self, target):
        for irow, row in enumerate(self.virtual_data):
            for icell, cell in enumerate(row):
                if cell == target:
                    self.virtual_data[irow][icell] = "X"

    def check_for_win(self):
        for row in self.virtual_data:
            if len(set(row)) == 1:
                return True
        _transpose_data = np.transpose(self.virtual_data)
        for row in _transpose_data:
            if len(set(row)) == 1:
                return True
        return False

    def get_score(self, last_draw):
        _flatten_data = np.ravel(self.virtual_data)
        return sum(int(data) for data in _flatten_data if data != "X") * int(last_draw)

    def reset(self):
        self.virtual_data = self.data


def solution1(draws, boards):
    _draws = draws.copy()
    while _draws:
        current_draw = _draws.pop(0)
        for board in boards:
            board.mark(current_draw)
            if board.check_for_win():
                return board.get_score(current_draw)


def solution2(draws, boards):
    _draws = draws.copy()
    _boards = boards.copy()
    while _draws and _boards:
        current_draw = draws.pop(0)
        for board in _boards:
            board.mark(current_draw)

        for i, board in enumerate(_boards):
            if board.check_for_win():
                winner = _boards.pop(i)
    return winner.get_score(current_draw)


if __name__ == "__main__":
    # Find dir address where the current code located and read input.txt from the dir
    dir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(dir, "input.txt")) as file:
        data = file.read().splitlines()
    draws = data[0].split(",")
    boards = [Board(data[i + 1 : i + 6]) for i, line in enumerate(data) if line == ""]

    print(solution1(draws, boards))
    for board in boards:
        board.reset()
    print(solution2(draws, boards))
