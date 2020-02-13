from board_utils import *

def choose_first_mover():
    msg = 'Please choose first player (x/o): '
    player = '-'
    while player != 'x' and player != 'o':
        player = input(msg).strip().lower()
        if player != 'x' and player != 'o':
            msg = 'Please choose either x or o: '
    return player

def play(board):
    print('Computer is x')
    player = choose_first_mover()
    result = game_over(board)
    while not result:
        if player == 'x':
            board = make_computer_move(board)
            show_board(board)
            print()
            player = 'o'
        else:
            board = make_human_move(board)
            show_board(board)
            print()
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
        ['-', '-', '-'],
        ['-', '-', '-'],
        ['-', '-', '-']]
    play(board)
