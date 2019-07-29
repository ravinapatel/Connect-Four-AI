'''
CONNECT FOUR - GUI
NAME: Ravina Patel
STARTED: June 21, 2019
'''

import tkinter as tk
from constants import *
from tkinter import Tk, Canvas, Frame, Label, BOTH
from connect_four import Board, Game, Chip
import connect_four_ai as ai
import time

class Window:

    def __init__(self):
        self.size = dim
        self.root = Tk(className='Connect Four')
        self.state = 'waiting'
        self.cpu = True

        self.g = Game()
        self.b = Board()
        self.chip = None

        # Draw Upper Control Panel
        self.control = Frame(self.root, width=WIDTH, height=CONTROL_HEIGHT, bg=BACKGROUND_COLOR)
        self.control.pack(fill=tk.BOTH, expand=tk.YES)
        self.slide = Canvas(self.control, width = WIDTH, height = CHIP_PADDING*2 + CHIP_DIAMETER, bg = BACKGROUND_COLOR)
        self.slide.pack()

        # Draw Board
        self.canvas = Canvas(self.root, width=WIDTH, height=HEIGHT, bg=BOARD_COLOR, bd=0, highlightthickness=0)
        self.canvas.bind("<Button-1>", self.drop_chip)
        self.clear_board()
        self.canvas.pack()

        self.update()       # Constantly checks pointer position to move chip slider

        self.root.mainloop()

    # Clears all chips from the visual board display
    def clear_board(self):
        for row in range(self.size[0]):
            for col in range (self.size[1]):
                self.canvas.create_oval(PADDING_X+(CHIP_DIAMETER+CHIP_PADDING)*col, PADDING_Y+(CHIP_DIAMETER+CHIP_PADDING)*row, PADDING_X+(CHIP_DIAMETER+CHIP_PADDING)*col+CHIP_DIAMETER, PADDING_Y+(CHIP_DIAMETER+CHIP_PADDING)*row + CHIP_DIAMETER, fill=BACKGROUND_COLOR)


    def update(self):
        while self.state == 'waiting':
            self.root.update()          # Chip Slider
            self.x = self.root.winfo_pointerx() - self.root.winfo_rootx()
            if self.chip != None:
                self.slide.delete(self.chip)
            if self.g.turn%2 != 0:
                color = COLOR_P1
            else:
                color = COLOR_P2
            self.chip = self.slide.create_oval(self.x-CHIP_DIAMETER/2,CHIP_PADDING,CHIP_DIAMETER/2 + self.x,CHIP_PADDING+CHIP_DIAMETER, fill = color)

    # Resets everything for a new game
    def new_game(self, event):
        self.state='waiting'
        self.root.unbind('<Return>')
        self.canvas.delete(self.tint)
        self.canvas.delete(self.text1)
        self.canvas.delete(self.text2)
        self.canvas.delete(self.line)
        self.clear_board()
        self.b = Board()
        self.c = Board()
        self.g = Game()
        self.update()

    # Adds a chip to the correct column of the matrix
    def drop_chip(self, event):
        if not self.b.gameover:
            col_width = (WIDTH-PADDING_X*2)/dim[1]
            col = int((self.x-PADDING_X)//col_width)
            if self.b.chips[0][col] == 0:
                self.state == 'dropping'
                chip = self.g.create_chip()
                chip.drop_chip(self.b, col)
                self.draw_chip(chip,chip.pos[0],col)

    # Draws a chip on the visual board
    def draw_chip(self,chip,row,col):
        l=PADDING_X+(CHIP_DIAMETER+CHIP_PADDING)*col
        u=PADDING_Y+(CHIP_DIAMETER+CHIP_PADDING)*row
        r=PADDING_X+(CHIP_DIAMETER+CHIP_PADDING)*col+CHIP_DIAMETER
        d=PADDING_Y+(CHIP_DIAMETER+CHIP_PADDING)*row + CHIP_DIAMETER
        # for row in range(row):
            # self.canvas.create_oval(l,u,r,d,fill=chip.color)
            # time.sleep(0.2)
            # self.canvas.create_oval(l,u,r,d,fill=BACKGROUND_COLOR)
        self.canvas.create_oval(l,u,r,d,fill=chip.color)
        self.turn()

    # Checks if game is over and starts the next move
    def turn(self):
        check = self.b.check()
        if self.b.gameover == True:      # New Game
            self.state = 'gameover'
            self.gameover(check)
        else:
            self.g.turn += 1
            if self.g.turn == 43:
                self.state = 'gameover'
                self.gameover()
            if self.cpu:
                if self.g.turn%2 == 0:
                    self.cpu_drop_chip()


    # Adds a chip to the column of the matrix determined by ai
    def cpu_drop_chip(self):
        if not self.b.gameover:
            col = ai.minimax(self.g,self.b,4,True)[0]
            self.state == 'dropping'
            chip = self.g.create_chip()
            chip.drop_chip(self.b, col)
            self.draw_chip(chip,chip.pos[0],col)

    # Draws a line through a 4-in-a-row
    def draw_line(self, direction, pos):
        row1 = pos[0]
        col1 = pos[1]
        row2 = pos[2]
        col2 = pos[3]
        x1 = PADDING_X+(CHIP_DIAMETER+CHIP_PADDING)*col1
        y1 = PADDING_Y+(CHIP_DIAMETER+CHIP_PADDING)*row1
        x2 = PADDING_X+(CHIP_DIAMETER+CHIP_PADDING)*col2 + CHIP_DIAMETER
        y2 = PADDING_Y+(CHIP_DIAMETER+CHIP_PADDING)*row2 + CHIP_DIAMETER

        if direction == 'h':
            x1 -= CHIP_PADDING/2
            y1 += CHIP_DIAMETER/2
            x2 += CHIP_PADDING/2
            y2 -= CHIP_DIAMETER/2
        elif direction == 'v':
            x1 += CHIP_DIAMETER/2
            y1 += CHIP_DIAMETER + CHIP_PADDING/2
            x2 -= CHIP_DIAMETER/2
            y2 -= CHIP_DIAMETER + CHIP_PADDING/2
        elif direction == 'p':
            y1 += CHIP_DIAMETER
            y2 -= CHIP_DIAMETER

        self.line = self.canvas.create_line(x1, y1, x2, y2, fill=LINE_COLOR)

    def gameover(self,check):
        self.draw_line(check[0],check[1])
        self.tint = self.canvas.create_rectangle(0,0,WIDTH,HEIGHT,fill="white", stipple='gray50')
        self.text1 = self.canvas.create_text(WIDTH/2,HEIGHT/2-30,text='Game Over',font=('Helvetica', 50, 'bold'),fill='black')
        self.text2 = self.canvas.create_text(WIDTH/2,HEIGHT/2+30,text='Press ENTER to play again',font=('Helvetica', 25, 'bold'),fill='black')
        self.root.bind('<Return>', self.new_game)


w = Window()
