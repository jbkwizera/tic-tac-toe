import copy
import random
from minmax import *

#-----------------------board functions ----------------------------------------
def get_next_positions(board, player):
    next_positions = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == '-':
                temp = copy.deepcopy(board)
                temp[i][j] = player
                next_positions.append(temp)
    return next_positions

def show_board(board):
    print('{:^3s}|{:^3s}|{:^3s}'.format(board[0][0], board[0][1], board[0][2]))
    print('---|---|---')
    print('{:^3s}|{:^3s}|{:^3s}'.format(board[1][0], board[1][1], board[1][2]))
    print('---|---|---')
    print('{:^3s}|{:^3s}|{:^3s}'.format(board[2][0], board[2][1], board[2][2]))

#---------------------utility functions ----------------------------------------
def make_computer_move(board, player='x'):
    print('Computer\'s turn')
    next_positions = get_next_positions(board, player)
    if player == 'x':
        pos_evaluation = [evaluate_ab(pos, 'o', -10, +10) for pos in next_positions]
        best_move_position = max(zip(pos_evaluation, next_positions))[1]
    else:
        pos_evaluation = [evaluate_ab(pos, 'x', -10, +10) for pos in next_positions]
        best_move_position = min(zip(pos_evaluation, next_positions))[1]
    return best_move_position

def make_human_move(board):
    msg  = 'Your turn: '
    while True:
        move = input(msg)
        try:
            i, j = [int(coord) for coord in move.strip()]
        except ValueError:
            msg = 'Please enter your move as ij (ex: 00): '
        else:
            if i < 0 or i >= 3 or j < 0 or j >= 3:
                msg = 'Please enter a correct cell: '
            elif board[i][j] != '-':
                msg = 'Please enter an unoccupied cell: '
            else:
                board[i][j] = 'o'
                return board

def make_random_move(board, player='o'):
    unoccupied_cells = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == '-':
                unoccupied_cells.append((i, j))
    i, j = random.choice(unoccupied_cells)
    board[i][j] = 'o'
    return board

def choose_first_mover():
    msg = 'Please choose first player (x/o): '
    player = '-'
    while player != 'x' and player != 'o':
        player = input(msg).strip().lower()
        if player != 'x' and player != 'o':
            msg = 'Please choose either x or o: '
    return player

def choose_first_mover_random():
    return 'x' if random.random() < 0.5 else 'o'

def game_over(board):
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
