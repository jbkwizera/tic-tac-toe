import copy

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

def make_computer_move(board):
    from minmax import evaluate_ab

    print('Computer\'s turn: ')
    next_positions = get_next_positions(board, 'x')
    pos_evaluation = [evaluate_ab(pos, 'o', -10, +10) for pos in next_positions]
    best_move_position = max(zip(pos_evaluation, next_positions))[1]
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
