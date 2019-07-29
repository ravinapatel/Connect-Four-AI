'''
CONNECT FOUR - MODELS
NAME: Ravina Patel
STARTED: June 21, 2019
'''
import numpy as np
from constants import *

class Board():

    def __init__(self,chips=np.zeros((dim[0],dim[1])),copy=False):
        if not copy:
            self.chips = np.zeros((dim[0],dim[1]))
        else:
            self.chips = chips
        self.gameover = False

    def pretty_print(self):
        print('_'*20)
        for row in self.chips:
            print(row)
        print('_'*20)

    # Creates a new Board object with the same chips array
    def copy(self):
        return Board(np.copy(self.chips),True)

    def check_horiz(self,n=4,virtual=False):
        for row in range(len(self.chips)):
            for col in range(len(self.chips[0])-3):
                if self.chips[row][col] == self.chips[row][col+1] == self.chips[row][col+2] == self.chips[row][col+3] != 0:
                    self.gameover = True
                    self.winner = self.chips[row][col]
                    return [row,col,row,col+3]

    def check_vert(self,n=4,virtual=False):
        for row in range(3,len(self.chips)):
            for col in range(len(self.chips[1])):
                if self.chips[row][col] == self.chips[row-1][col] == self.chips[row-2][col] == self.chips[row-3][col] != 0:
                    self.gameover = True
                    self.winner = self.chips[row][col]
                    return [row,col,row-3,col]

    def check_pos(self):
        for row in range(3,len(self.chips)):
            for col in range(len(self.chips[0])-3):
                if self.chips[row][col] == self.chips[row-1][col+1] == self.chips[row-2][col+2] == self.chips[row-3][col+3] != 0:
                    self.gameover = True
                    self.winner = self.chips[row][col]
                    return [row,col,row-3,col+3]

    def check_neg(self):
        for row in range(len(self.chips)-3):
            for col in range(len(self.chips[0])-3):
                if self.chips[row][col] == self.chips[row+1][col+1] == self.chips[row+2][col+2] == self.chips[row+3][col+3] != 0:
                    self.gameover = True
                    self.winner = self.chips[row][col]
                    return [row,col,row+3,col+3]

    # Checks all directions for 4-in-a-row and returns a winning direction
    def check(self,n=4):
        h = 'h',self.check_horiz()
        v = 'v',self.check_vert()
        p = 'p',self.check_pos()
        n = 'n',self.check_neg()
        for check in [h,v,p,n]:
            if check[1] != None:
                return check


class Chip():

    def __init__(self, player=1):
        self.player = player
        if self.player == 1:
            self.color = COLOR_P1
        else:
            self.color = COLOR_P2

    def drop_chip(self, board, column):
        '''
        Find the lowest empty spot in the specified column and
        '''
        for row in range(len(board.chips)):
            if board.chips[row][column] != 0:
                self.pos = [row-1,column]
                board.chips[self.pos[0]][self.pos[1]] = self.player
                return
        self.pos = [dim[0]-1,column]
        board.chips[self.pos[0]][self.pos[1]] = self.player


class Game():

    def __init__(self):
        self.turn = 1

    # Creates a chip object of the correct color
    def create_chip(self):
        if self.turn%2 != 0:
            return Chip(1)
        else:
            return Chip(2)
