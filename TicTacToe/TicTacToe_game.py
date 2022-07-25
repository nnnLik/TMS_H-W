import tkinter
import random

class TicTacToe(tkinter.Canvas):
    def __init__(self, window):
        super().__init__(window, width=300, height=300)
        self.state = [None, ] * 9
        self.bind('', self.click)

    def get_winner(self):
        variants = []

        # колонки и столбцы
        for i, j in enumerate(range(0, 9, 3)):
            variants.append(self.state[j:j + 3])
            variants.append(self.state[i::3])

        # две диагонали
        variants.append(self.state[::4])
        variants.append(self.state[2:7:2])

        if ['x', ] * 3 in variants:
            return 'x_win'
        elif ['o', ] * 3 in variants:
            return 'o_win'
        elif None not in self.state:
            return 'draw'

    def bot_move(self):
        indexes = []
        for index, e in enumerate(self.state):
            if e is None:
                indexes.append(index)
        index = random.choice(indexes)
        self.state[index] = 'o'
        self.add_o(index % 3, int(index / 3))

    def click(self, event):
        column = int(event.x / 100)
        row = int(event.y / 100)
        index = row * 3 + column
        if self.state[index] is None:
            self.state[index] = 'x'
            self.add_x(column, row)
            self.bot_move()


    def add_x(self, column, row):
        self.create_line(
            column * 100 + 20,
            row * 100 + 20,
            column * 100 + 80,
            row * 100 + 80,
            width=5,
            fill='dark blue'
        )
        self.create_line(
            column * 100 + 80,
            row * 100 + 20,
            column * 100 + 20,
            row * 100 + 80,
            width=5,
            fill='dark blue'
        )

    def add_o(self, column, row):
        self.create_oval(
            column * 100 + 20,
            row * 100 + 20,
            column * 100 + 80,
            row * 100 + 80,
            width=5,
            outline='dark salmon'
        )

tk_window = tkinter.Tk()
game = TicTacToe(tk_window)
game.pack()

tk_window.mainloop()