from game import Game
class GameTesting(Game):
    def __init__(self, board=None):
        super().__init__(board)

    #-------------------------------machine vs. machine-------------------------
    def machine_vs_machine(self):
        self.reset()
        self._player = self.choose_first_mover_random()
        while True:
            self.make_computer_move(self._player)
            if self.game_over():
                return self.evaluate('x')

    #------------------------------machine vs random----------------------------
    def machine_vs_random(self):
        self.reset()
        self._player = self.choose_first_mover_random()
        while True:
            if self._player=='x':
                self.make_computer_move()
            else:
                self.make_random_move()
            if self.game_over():
                return self.evaluate('x')

    #-------------------------------man vs. machine-----------------------------
    def man_vs_machine(self):
        self.reset()
        self._player = 'o' if input("Do you to go first? y/n: ")=='y' else 'x'
        result = self.game_over()
        while not result:
            if self._player == 'x':
                move = self.get_best_move('x')
                print('Computer: ', ''.join(str(x) for x in move))
                self.make_computer_move()
                print(self)
            else:
                move = input('Your move (ex. 00): ')
                move = [int(x) for x in move.strip()]
                self.make_human_move(move)
                print(self)
            print()
            result = self.game_over()

        # show game result
        if result == 'x':
            print('Computer won!')
        elif result == 'o':
            print('You won! (Good luck with that!)')
        elif result == 'd':
            print('Game drawn!')


if __name__ == '__main__':
    gt = GameTesting()

    counts = [0, 0, 0] # losses-draws-wins
    for t in range(10):
        counts[gt.machine_vs_random()+1] += 1
    print(counts)

    ############################################################################
    # machine_vs_machine    all games are drawn.
    # machine_vs_random     on average, computer wins 89%, draws 11% and loses 0%
    # man_vs_machine        same result as machine_vs_machine with optimal play
    ############################################################################
    #                             v1.0 inheritance tree
    #                                ----------------
    #                               |    base.py    |
    #                               ----------------
    #                                       |
    #                                ----------------
    #                               |    board.py   |
    #                               ----------------
    #                                       |
    #                                ----------------
    #                               |    game.py    |
    #                               ----------------
    #                                       |
    #                           ------------------------
    #                          |                       |
    #                 -------------------       --------------
    #                | game_testing.py  |      | gameUI.py   |
    #                -------------------       --------------
    #
    ############################################################################
