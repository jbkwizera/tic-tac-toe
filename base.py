from abc import ABCMeta, abstractmethod

class Base(metaclass=ABCMeta):
    #-------------------------------universal methods---------------------------
    @classmethod
    def __init__(self, board=None):
        """Initialize booard to starting position or a given position."""

        if not board:
            self._board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        else:
            self._board = board

    #------------------------------abstract methods-----------------------------
    @abstractmethod
    def evaluate(self, player):
        """Return evaluation of current position for the given player."""

    @abstractmethod
    def get_positions(self, player):
        """Return all possible positions for the given player."""

    @abstractmethod
    def get_best_move(self, player):
        """Return best move for the given player."""

    @abstractmethod
    def get_best_position(self, player):
        """Return best position for the given player."""
