'''
CONNECT FOUR - MODELS
NAME: Ravina Patel
STARTED: June 21, 2019
'''
import numpy as np
from constants import *

class Board():

    def __init__(self):
        self.chips = np.zeros((6,7))
        # self.chips[4][4] = 1
        # self.chips[3][5] = 1
        # self.chips[2][6] = 1

        # self.chips[5][1] = 1
        # self.chips[4][2] = 1
        # self.chips[3][3] = 1
        # self.chips[3][4] = 1
        # self.chips[2][4] = 1

        self.gameover = False

    def pretty_print(self):
        print('_'*20)
        for row in self.chips:
            print(row)
        print('_'*20)

    def check_horiz(self,n=4,virtual=False):
        # for row in range(len(self.chips)):
        #     for col in range(len(self.chips[0])-3):
        #         if self.chips[row][col] == self.chips[row][col+1] == self.chips[row][col+2] == self.chips[row][col+3] != 0:
        #             self.gameover = True
        #             print('win')
        # print('checking')
        for row in range(len(self.chips)):
            for col in range(len(self.chips[0])-n+1):
                temp = self.chips[row][col]
                count = 1
                for i in range(1,n):
                    if temp != 0 and temp == self.chips[row][col+i]:
                        count +=1
                    if count == n:
                        print(n,'in a row')
                        if virtual:
                            return row,col
                        else:
                            self.gameover = True
                            print('win')
        return None

    def check_vert(self,n=4,virtual=False):
        temp = self.chips
        self.chips = self.chips.transpose()
        x = self.check_horiz(n,virtual)
        self.chips = temp
        if x != None:
            return x

    # def check_pos(self):
    #     for row in range(3,len(self.chips)+1):
    #         for col in range(len(self.chips[0])-3):
    #             try:
    #                 if self.chips[row][col] == self.chips[row-1][col+1] == self.chips[row-2][col+2] == self.chips[row-3][col+3] != 0:
    #                     self.gameover = True
    #                     print('win')
    #             except:
    #                 pass

    def check_pos(self,n=4,virtual=False):
        result = []
        for row in range(3,len(self.chips)):
            for col in range(len(self.chips[0])-3):
                temp = self.chips[row][col]
                count = 1
                for i in range(1,n):
                    if virtual:
                        if temp == 0 and self.chips[row-i][col+i] != 0:
                            temp = self.chips[row-i][col+i]
                    if temp != 0 and temp == self.chips[row-i][col+i]:
                        count +=1
                    if count == n:
                        print(n,'in a row')
                        if virtual:
                            result.append((row,col))
                        else:
                            self.gameover = True
                            print('win')
        if virtual:
            return result
        # print(count)
                # if self.chips[row][col] == self.chips[row-1][col+1] == self.chips[row-2][col+2] == self.chips[row-3][col+3] != 0:
                #     self.gameover = True
                #     print('win')

    def check_neg(self):
        for row in range(3):
            for col in range(4):
                try:
                    if self.chips[row][col] == self.chips[row+1][col+1] == self.chips[row+2][col+2] == self.chips[row+3][col+3] != 0:
                        self.gameover = True
                        print('win')
                except:
                    print('win')
                    self.gameover= True
                    print(self.gameover)
                    pass


    def check(self,n=4):
        self.check_horiz(n)
        self.check_vert(n)
        self.check_pos(n)
        self.check_neg()



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
        self.pos = [5,column]
        board.chips[self.pos[0]][self.pos[1]] = self.player

class Game():

    def __init__(self):
        self.turn = 1

    def create_chip(self):
        if self.turn%2 != 0:
            return Chip(1)
        else:
            return Chip(2)
