from board import Board
import random

class Game(Board):
    def __init__(self, board=None):
        super().__init__(board)
        self._player = 'o'
        self._moveN  = 0

    #------------------------------choose first mover---------------------------
    def choose_first_mover(self, player='o'):
        self._player = player


    def choose_first_mover_random(self):
        return 'x' if random.random() < 0.5 else 'o'

    #------------------------------move by ai-----------------------------------
    def make_computer_move(self, comp='x'):
        # computer plays x when playing against human or random

        i, j = self.get_best_move(comp)
        self._board[i][j] = comp
        self._player = 'o' if comp=='x' else 'x'
        self._moveN += 1

    #------------------------------move by user---------------------------------
    def make_human_move(self, move):
        # human plays o when playing against computer

        i, j = move
        # ignore invalid moves
        if self._board[i][j] != '-' or (i < 0 or i > 2 or j < 0 or j > 2):
            return
        self._board[i][j] = 'o'
        self._player = 'x'
        self._moveN += 1

    #---------------------------random move ------------------------------------
    def make_random_move(self):
        # random plays o when playing against computer

        unoccupied_cells = []
        for i in range(3):
            for j in range(3):
                if self._board[i][j] == '-':
                    unoccupied_cells.append((i, j))
        i, j = random.choice(unoccupied_cells)
        self._board[i][j] = 'o'
        self._player = 'x'
        self._moveN += 1


    #--------------------------------reset game---------------------------------
    def reset(self):
        self._board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        self._player= 'o'
        self._moveN = 0


if __name__ == '__main__':
    b = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
