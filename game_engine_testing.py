from board_utils import *
import sys

def play_game(board):
    player = choose_first_mover_random()
    result = game_over(board)
    while not result:
        if player == 'x':
            board  = make_computer_move(board, 'x')
            player = 'o'
        else:
            board  = make_computer_move(board, 'o')
            player = 'x'
        result = game_over(board)
    return result

def main(N):
    count = [0]*3
    for n in range(N):
        board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        result = play_game(board)
        if result == 'x':
            count[0] += 1
        elif result == 'o':
            count[1] += 1
        elif result == 'd':
            count[2] += 1

    print('{:>8s}|{:>8s}|{:>8s}|{:>8s}'.format("wins", "losses", "draws", "games"))
    print('-' * 35)
    print('{:>8d}|{:>8d}|{:>8d}|{:>8d}'.format(count[0], count[1], count[2], N))
    print('-' * 35)
    print('{:>8.2f}|{:>8.2f}|{:>8.2f}|{:>8.2f}'.format(100*count[0]/N, 100*count[1]/N, 100*count[2]/N, 100))

if __name__ == '__main__':
    board = [
        ['x', '-', '-'],
        ['-', 'o', '-'],
        ['-', 'x', '-']]
    main(int(sys.argv[1]))
