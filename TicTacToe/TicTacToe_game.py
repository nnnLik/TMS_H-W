
import tkinter
import random
import time

class TicTacToe(tkinter.Canvas):
    def __init__(self,window):
        super().__init__(window,width=300,height=300)
        self.state = [None,None,None,None,None,None,None,None,None]
        self.bind('<Button-1>', self.click)

    def draw_lines(self):
        self.create_line(100,0,100,300)
        self.create_line(200,0,200,300)
        self.create_line(0,100,300,100)
        self.create_line(0,200,300,200)




    def click(self,event):
        column = int(event.x / 100)
        row = int(event.y / 100)
        index = row * 3 + column
        if self.state[index] is None:
            self.state[index] = 'x'
            self.add_x(column, row)
            is_NoneX = self.get_winner()
            if is_NoneX == None:
                self.bot_move()
                is_NoneO = self.get_winner()
                if is_NoneO:
                    self.on_event(is_NoneO)
                elif is_NoneO == 'draw':
                    self.on_event(is_NoneO)

            elif is_NoneX == "draw":
                self.on_event(is_NoneX)
            else:
                self.on_event(is_NoneX)

    def on_event(self,text):
        self.text = text
        self.delete("all")
        self.create_text(150,150,text=text)
        time.sleep(3)
        #then delete text to restart the game
        self.delete("all")
        self.state = [None] * 9
        self.draw_lines()


    def bot_move(self):

        while True:
            rand_index = random.randrange(len(self.state))
            is_empty = self.state[rand_index]

            if is_empty == None:
                self.state[rand_index] = "o"
                print(self.state)
                break

        column = int(rand_index % 3)
        row = int(rand_index / 3)

        self.add_o(column,row)
        self.get_winner()

    def get_winner(self):
        #first column
        win_line = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
        for list_ in win_line:
            chars = []
            for index in list_:
                chars.append(self.state[index])

                if len(chars) == 3:
                    res = chars.count(chars[0]) == len(chars)
                    #if res == True, then all chars are same
                    if res:
                        get_char = chars[0]
                        if get_char == "x":
                            return "x_win"
                        elif get_char == 'o':
                            return "o_win"

        if None not in self.state:
            return "draw"

        else:
            return None






    def add_o(self,column,row):

        self.create_oval(
            column * 100 + 20,
            row * 100 + 20,
            column * 100 + 80,
            row * 100 + 80,width=5,
            outline="orange")

    def add_x(self,column,row):
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



window = tkinter.Tk()
game = TicTacToe(window)
game.pack()
game.draw_lines()

window.mainloop()