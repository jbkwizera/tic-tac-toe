import copy
import re
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
    for i in range(3):
        for j in range(3):
            print(board[i][j], end=' ')
        print()

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
    if (board[0][0] == board[1][1] == board[2][2] or \
        board[2][0] == board[1][1] == board[0][2]) and board[1][1] != '-':
        return board[1][1]

    # game is drawn
    if draw: return 'd'

    # game is not over
    return False

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

def make_computer_move(board):
    print('Computer\'s turn: ')
    next_positions = get_next_positions(board, 'x')
    pos_evaluation = [evaluate(pos, 'o') for pos in next_positions]
    best_move_position = max(zip(pos_evaluation, next_positions))[1]
    return best_move_position

def make_human_move(board):
    msg  = 'Your turn: '
    while True:
        move = input(msg)
        try:
            i, j = [int(coord) for coord in list(move.strip())]
        except ValueError:
            msg = 'Please enter move as ij (ex: 00): '
        else:
            if i < 0 or i >= 3 or j < 0 or j >= 3:
                msg = 'Please enter a correct cell: '
            elif board[i][j] != '-':
                msg = 'Please enter an unoccupied cell: '
            else:
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

def play_game(board=[['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]):
    print('Computer is x')
    player = choose_first_mover()
    result = game_over(board)
    while not result:
        if player == 'x':
            board = make_computer_move(board)
            show_board(board)
            print('-' * 16)
            player = 'o'
        else:
            board = make_human_move(board)
            show_board(board)
            print('-' * 16)
            player = 'x'
        result = game_over(board)

    # show game result
    if result == 'x':
        print('Computer won!')
    elif result == 'o':
        print('You won! (Good luck with that!)')
    elif result == 'd':
        print('Game drawn!')


if __name__ == '__main__':
    board = [
        ['x', '-', '-'],
        ['-', 'o', '-'],
        ['-', 'x', '-']]
    play_game()
