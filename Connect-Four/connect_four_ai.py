'''
CONNECT FOUR - AI
NAME: Ravina Patel
STARTED: June 21, 2019
'''
import numpy as np
from constants import *
from connect_four import Board, Game, Chip
from random import randint


def randomBot(board):
    print('randomBot')
    col = randint(0,dim[0])
    if board.chips[0][col] == 0:
        return col
    else:
        randomBot(board)

def aggressiveBot(board):
    # Checking for 3 horizontal in a row
    n=3
    print('checking horiz')
    if board.check_horiz(n,True) != None:
        print('horizontal found')
        row,col = board.check_horiz(3,True)
        # Checking if it is a direct threat
        if col+n != dim[1]:
            if board.chips[row][col+n] == 0 and (row == dim[0]-1 or board.chips[row+1][col+n] != 0):
                print('right')
                return col+n
        if col != 0:
            if board.chips[row][col-1] == 0 and (row == dim[0]-1 or board.chips[row+1][col-1] != 0):
                print('left')
                return col-1

    # Checking for 3 vertical in a row
    print('checking vert')
    if board.check_vert(3,True) != None:
        print('vertical found at')
        col,row = board.check_vert(3,True)
        print(row,col)
        if board.chips[row-1][col] == 0:
            print('returning a vertical block')
            return col

    # Checking for 3 pos diag in a row
    print('checking pos')
    if len(board.check_pos(3,True)) != 0:
        for pos in board.check_pos(3,True):
            print('pos found at')
            row,col = pos
            print(row,col)
            # Checking top right
            if col != len(board.chips[0])-1 and row != 0:
                if board.chips[row-n][col+n] == 0 and board.chips[row-n+1][col+n] != 0:
                    print('top right')
                    return col+n
            # Checking bottom left
            # if col != 0 and row != len(board.chips)-1:
            print('starting')
            if board.chips[row][col] == 0 and (row == dim[0]-1 or board.chips[row+2][col] != 0):
                print('bottom left')
                return col


    # Random if no direct threat
    # randomBot(board)

    print('Random Placement')
    col = randint(0,dim[0])
    if board.chips[0][col] == 0:
        return col
    else:
        aggressiveBot(board)
