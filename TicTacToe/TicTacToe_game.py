import tkinter

class TicTacToe(tkinter.Canvas):
    def __init__(self, window):
        super().__init__(window, width=300, height=300)


tk_window = tkinter.Tk()
game = TicTacToe(tk_window)
game.pack()

tk_window.mainloop()