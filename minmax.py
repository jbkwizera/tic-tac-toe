import copy
import re
def next_positions(board, player):
    next = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == '-':
                temp = copy.deepcopy(board)
                temp[i][j] = player
                next.append(temp)
    return next

def show_board(board):
    for i in range(3):
        for j in range(3):
            print(board[i][j] if board[i][j] else '-', end=' ')
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

    if draw: return 'd'

    return False

def evaluate(board, player):
    result = game_over(board)
    if result:
        if result == 'x': return +1
        if result == 'o': return -1
        return 0
    elif player == 'x':
        return max(evaluate(position, 'o') for position in next_positions(board, 'x'))
    else:
        return min(evaluate(position, 'x') for position in next_positions(board, 'o'))

def make_move(board):
    next   = next_positions(board, 'x')
    values = [evaluate(position, 'o') for position in next]
    best_next_position = max(zip(values, next))[1]
    return best_next_position

def play(board):
    print('Computer is x')
    player  = '-'
    request = 'Please choose first player (x/o): '
    while player != 'x' and player != 'o':
        player = input(request).strip().lower()
        if player != 'x' and player != 'o':
            request = 'Please choose either x or o: '

    while True:
        result = game_over(board)
        if result:
            if result == 'x':
                print('Computer won!')
            elif result == 'o':
                print('You won! (Good luck with that!)')
            else:
                print('Draw! (That\'s an achievement!)')
            break
        else:
            if player == 'x':
                print('Computer\'s turn')
                board = make_move(board)
                show_board(board)
                print('-' * 10)
                player = 'o'
            else:
                move = input('Your turn. enter location in the matrix: ')
                i, j = [int(coord) for coord in re.split('', move.strip()) if coord]
                board[i][j] = 'o'
                show_board(board)
                print('-' * 10)
                player = 'x'


if __name__ == '__main__':
    board = [
        ['-', '-', '-'],
        ['-', '-', '-'],
        ['-', '-', '-']]

    play(board)
