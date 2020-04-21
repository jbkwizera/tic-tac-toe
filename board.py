from base import Base
class Board(Base):

    def __init__(self, board=None):
        super().__init__(board)

    #----------------------------minimax methods -------------------------------
    def evaluate(self, player='x'):
        """Return evaluation of current position for the given player.
           evaluation = +1: player wins
           evaluation = -1: player loses
           evaluation =  0: game is a draw
        """
        eval = self._evaluate(self._board, player, -10, 10)
        return eval

    def _evaluate(self, board, player, a, b):
        """Internal work for evaluate method."""

        result = self.game_over(board)
        if result:
            if result == 'x': return +1
            if result == 'o': return -1
            return 0
        elif player == 'x':
            value = -10
            for pos in self._get_positions(board, 'x'):
                value = max(value, self._evaluate(pos, 'o', a, b))
                a = max(a, value)
                if a >= b:
                    break
            return value
        else:
            value = +10
            for pos in self._get_positions(board, 'o'):
                value = min(value, self._evaluate(pos, 'x', a, b))
                b = min(b, value)
                if a >= b:
                    break
            return value

    #-------------------------------position methods----------------------------
    def get_positions(self, player='x'):
        """Return all possible positions starting from current position"""
        return self._get_positions(self._board, player)

    def _get_positions(self, board, player='x'):
        import copy
        positions = []
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    temp = copy.deepcopy(board)
                    temp[i][j] = player
                    positions.append(temp)
        return positions

    #----------------------------best move/position methods---------------------
    def get_best_move(self, player='x'):
        """Return best move for the given player."""
        return self._get_best_move_and_position(self._board, player)[0]

    def get_best_position(self, player='x'):
        """Return best position for the given player."""
        return self._get_best_move_and_position(self._board, player)[1]

    def _get_best_move_and_position(self, board, player='x'):
        """Internal work for both get_best_move and get_best_position"""

        positions = self._get_positions(board, player)
        if player == 'x':
            pos_evals = [self._evaluate(pos, 'o', -10, +10) for pos in positions]
            best_pos  = max(zip(pos_evals, positions))[1]
        else:
            pos_evals = [self._evaluate(pos, 'x', -10, +10) for pos in positions]
            best_pos  = min(zip(pos_evals, positions))[1]
        for i in range(3):
            for j in range(3):
                if board[i][j] != best_pos[i][j]:
                    return ([i, j], best_pos)

    #------------------------------board state ---------------------------------
    def game_over(self, board=None):
        """Return false if the game is over as given by board position.
           Otherwise, return game's state.
           x: x wins (equiv. o loses)
           o: o wins (equiv. x loses)
           d: draw
           Optional argument board is necessary to accomondate the recursive
           nature of the minimax/self._evaluate method.
        """

        if not board:
            board = self._board
        draw = True
        for i in range(3):
            countx = [0, 0] # horizontal, vertical
            counto = [0, 0] # horizontal, vertical
            for j in range(3):
                if board[i][j] == 'x': countx[0] += 1
                if board[j][i] == 'x': countx[1] += 1
                if board[i][j] == 'o': counto[0] += 1
                if board[j][i] == 'o': counto[1] += 1
                if board[i][j] == '-': draw = False
            if countx[0] == 3 or countx[1] == 3: return 'x'
            if counto[0] == 3 or counto[1] == 3: return 'o'

        # check diagonals
        if  (board[0][0] == board[1][1] == board[2][2]) or \
            (board[2][0] == board[1][1] == board[0][2]):
            if board[1][1] != '-':
                return board[1][1]

        # game is drawn
        if draw: return 'd'

        # game is not over
        return False

    #-----------------------------show board------------------------------------
    def __str__(self):
        """Print out current board position on stdin. Useful for console-based UI."""

        s  = '{:^3s}|{:^3s}|{:^3s}\n'.format(self._board[0][0], self._board[0][1], self._board[0][2])
        s += '---|---|---\n'
        s += '{:^3s}|{:^3s}|{:^3s}\n'.format(self._board[1][0], self._board[1][1], self._board[1][2])
        s += '---|---|---\n'
        s += '{:^3s}|{:^3s}|{:^3s}  '.format(self._board[2][0], self._board[2][1], self._board[2][2])
        return s
