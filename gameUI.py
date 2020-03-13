from game import Game
import tkinter as tk
from tkinter import font

class GameUI(Game):
    def __init__(self, board=None):
        """Game launcher"""

        super().__init__(None)

        #-------------------------------main frame------------------------------
        root = tk.Tk()
        root.title("Tic Tac Toe")
        root.configure(bg="lightgray")
        self._main = tk.Frame(master=root, bg="lightgray")
        self._main.configure(bg="lightgray")
        moveFont = font.Font(family="Comic Sans MS", size="70")

        # choose/play buttons container
        header_frm = tk.Frame(master=self._main, bg="lightgray")
        header_frm.pack()

        #------------------------------choose button----------------------------
        choose_frm = tk.Frame(master=header_frm, relief=tk.RAISED, borderwidth=1, cursor="hand")
        choose_lbl = tk.Label(master=choose_frm, text="Click to move second", bg="red", fg="white")
        choose_lbl.message = "choose"

        # choose first player
        def choose(event):
            if self._moveN == 0:
                lbl = choose_lbl.cget("text")
                if "first" in lbl:
                    choose_lbl.configure(text="Click to move second")
                    self._player = 'o'
                else:
                    choose_lbl.configure(text="Click to move first")
                    self._player = 'x'
                    self.play(event)

        choose_lbl.bind("<Button-1>", choose)
        choose_lbl.pack(ipadx=10, ipady=10)
        choose_frm.pack(side=tk.LEFT, padx=10, pady=10)

        #-------------------------------reset button----------------------------
        reset_frm = tk.Frame(master=header_frm, relief=tk.RAISED, borderwidth=1, cursor="hand")
        reset_lbl = tk.Label(master=reset_frm, text="Reset", bg="red", fg="white")
        reset_lbl.message = "reset"

        # reset board and ui
        def reset(event):
            self.reset()
            for i in range(3):
                for cell_lbl in self._cells_lbls[i]:
                    cell_lbl.configure(text="")
                    cell_lbl.pack(ipadx=60, ipady=10)
            self._res_frm.pack_forget()
            choose_lbl.configure(text="Click to move second")

        reset_lbl.bind("<Button-1>", reset)
        reset_lbl.pack(ipadx=10, ipady=10)
        reset_frm.pack(side=tk.RIGHT, padx=10, pady=10)

        #----------------------------------board--------------------------------
        board_frm  = tk.Frame(master=self._main, relief=tk.RAISED, borderwidth=1, bg="lightgray")
        board_frm.pack(padx=72, pady=30)
        self._cells_lbls = []

        for i in range(3):
            row_lbls = []
            for j in range(3):
                cell_frm = tk.Frame(master=board_frm, height=120, width=120, relief=tk.RAISED, borderwidth=1, cursor="hand")
                cell_lbl = tk.Label(master=cell_frm, height=120, width=120)
                cell_lbl.message = 3*i + j              # cell id: 0...8
                cell_lbl.bind("<Button-1>", self.play)  # play on click
                cell_lbl.configure(font=moveFont)
                cell_lbl.pack()

                cell_frm.grid(row=i, column=j)
                cell_frm.pack_propagate(0)
                row_lbls.append(cell_lbl)
            self._cells_lbls.append(row_lbls)

        #------------------------------result frame-----------------------------
        self._res_frm = tk.Frame(master=self._main, relief=tk.RAISED, borderwidth=1)
        self._res_lbl = tk.Label(master=self._res_frm, text="", bg="red", fg="white")
        self._res_lbl.pack(ipadx=10, ipady=10)

        # launch gui
        self._main.pack(padx=32, pady=32)
        root.mainloop()

    def play(self, event):
        """Play event listener"""

        if self.game_over(): return

        if self._player == 'o':
            move = int(event.widget.message)
            move = [move//3, move % 3]
            self.make_human_move(move)
            if not self.game_over():
                self.make_computer_move()
        else:
            self.make_computer_move()
        if self.game_over():
            self.show_result()


    def make_human_move(self, move):
        """Override make_human_move to accomondate for updating GUI."""

        i, j = move
        if self._board[i][j] == 'x':
            return
        self._cells_lbls[i][j].configure(text='O')
        self._cells_lbls[i][j].pack(ipadx=32, ipady=10)
        self._board[i][j] = 'o'
        self._player = 'x'
        self._moveN += 1

    def make_computer_move(self):
        """Override make_computer_move to accomondate for updating GUI."""

        i, j = self.get_best_move()
        self._cells_lbls[i][j].configure(text='X')
        self._cells_lbls[i][j].pack(ipadx=35, ipady=10)
        self._board[i][j] = 'x'
        self._player = 'o'
        self._moveN += 1

    def show_result(self):
        result = self.game_over()
        if result == 'd':
            res_text = "Game drawn!"
        elif result == 'x':
            res_text = "Computer won!"
        else:
            res_text = "You won!"
        self._res_lbl.configure(text=res_text)
        self._res_frm.pack(padx=40)

if __name__ == '__main__':
    GameUI()
