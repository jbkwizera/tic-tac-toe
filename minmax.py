from board_utils import *

def evaluate(board, player):
    result = game_over(board)
    if result:
        if result == 'x': return +1
        if result == 'o': return -1
        return 0
    elif player == 'x':
        return max(evaluate(pos, 'o') for pos in get_next_positions(board, 'x'))
    else:
        return min(evaluate(pos, 'x') for pos in get_next_positions(board, 'o'))

def evaluate_ab(board, player, a, b):
    result = game_over(board)
    if result:
        if result == 'x': return +1
        if result == 'o': return -1
        return 0
    elif player == 'x':
        value = -10
        for pos in get_next_positions(board, 'x'):
            value = max(value, evaluate_ab(pos, 'o', a, b))
            a = max(a, value)
            if a >= b:
                break
        return value
    else:
        value = +10
        for pos in get_next_positions(board, 'o'):
            value = min(value, evaluate_ab(pos, 'x', a, b))
            b = min(b, value)
            if a >= b:
                break
        return value
