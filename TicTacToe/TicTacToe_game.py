import tkinter


class TicTacToe(tkinter.Canvas):

    def __init__(self, window):
        super().__init__(window, width=300, height=300)

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