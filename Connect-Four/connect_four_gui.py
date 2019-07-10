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
from time import sleep

class Window:

    def __init__(self):
        self.size = dim
        self.root = Tk(className='Connect Four')
        self.state = 'waiting'
        self.cpu = True

        self.g = Game()
        self.b = Board()
        self.b.pretty_print()
        self.chip = None

        # Draw Control Panel
        self.control = Frame(self.root, width=WIDTH, height=CONTROL_HEIGHT, bg=BACKGROUND_COLOR)
        self.control.pack(fill=tk.BOTH, expand=tk.YES)
        self.slide = Canvas(self.control, width = WIDTH, height = CHIP_PADDING*2 + CHIP_DIAMETER, bg = BACKGROUND_COLOR)
        self.slide.pack()

        # Draw Board
        self.canvas = Canvas(self.root, width=WIDTH, height=HEIGHT, bg=BOARD_COLOR, bd=0, highlightthickness=0)
        self.canvas.bind("<Button-1>", self.drop_chip)
        self.clear_board()
        self.canvas.pack()
        print('Turn:',self.g.turn)

        self.update()       # Constantly checks pointer position to move chip slider

        self.root.mainloop()

    # Clears all chips from the visual board
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
        print('resetting')
        self.state='waiting'
        self.root.unbind('<Return>')
        self.b = Board()
        self.g = Game()
        self.canvas.delete(self.tint)
        self.canvas.delete(self.text1)
        self.canvas.delete(self.text2)
        self.clear_board()
        self.update()

    # Adds a chip to the correct column of the matrix
    def drop_chip(self, event):
        if not self.b.gameover:
            col_width = (WIDTH-PADDING_X+CHIP_PADDING/2)/7
            col = int(self.x//col_width)
            if self.b.chips[0][col] == 0:
                self.state == 'dropping'
                chip = self.g.create_chip()
                chip.drop_chip(self.b, col)
                self.draw_chip(chip,chip.pos[0],col)


    # Adds a chip to the column of the matrix determined by ai
    def cpu_drop_chip(self):
        if not self.b.gameover:
            col = ai.aggressiveBot(self.b)
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
        self.canvas.create_oval(l,u,r,d,fill=chip.color)
        self.b.check()
        if self.b.gameover == True:      # New Game
            self.state = 'gameover'
            self.gameover()
        else:
            self.g.turn += 1
            if self.g.turn == 43:
                self.state = 'gameover'
                self.gameover()
            print('Turn:',self.g.turn)
            if self.cpu:
                if self.g.turn%2 == 0:
                    self.cpu_drop_chip()


    def gameover(self):
        print('gameover')
        self.tint = self.canvas.create_rectangle(0,0,WIDTH,HEIGHT,fill="white", stipple='gray50')
        self.text1 = self.canvas.create_text(WIDTH/2,HEIGHT/2-30,text='Game Over',font=('Helvetica', 50, 'bold'),fill='black')
        self.text2 = self.canvas.create_text(WIDTH/2,HEIGHT/2+30,text='Press ENTER to play again',font=('Helvetica', 25, 'bold'),fill='black')
        self.root.bind('<Return>', self.new_game)


w = Window()
