'''
CONNECT FOUR - AI
NAME: Ravina Patel
STARTED: June 21, 2019
'''
import numpy as np
from constants import *
from connect_four import Board, Game, Chip
from random import randint

AI = 2
HUMAN = 1

# Random AI
def randomBot(board):
    col = randint(0,dim[0])
    if board.chips[0][col] == 0:
        return col
    else:
        randomBot(board)

# Evaluates a baord state for AI
def score(board):
    score = 0
    copy = board.copy()
    copy.check()
    if copy.gameover:
        if copy.winner == 1:
            score += -1000
        elif copy.winner == 2:
            score += 1000000
    for row in range(dim[0]):
        if copy.chips[row][3] == 2:
            score += 4
    return score

# Checks which columns the AI can play in
def valid_col(board):
    result = []
    for col in range(dim[1]):
        if board.chips[0][col] == 0:
            result.append(col)
    return result

# Minimax AI
def minimax(game, board, depth, maxPlayer):
    copy1 = board.copy()
    copy1.check()
    if depth == 0 or copy1.gameover:
        return (None, score(board))
    if maxPlayer:
        bestValue = -1000000
        column = 3
        for col in valid_col(board):
            copy = board.copy()
            Chip(AI).drop_chip(copy, col)
            value = minimax(game,copy,depth-1, False)[1]
            if value > bestValue:
                bestValue = value
                column = col
        return column, bestValue

    else: # Minimizing Player
        bestValue = 1000000
        column = 3
        for col in valid_col(board):
            copy = board.copy()
            Chip(HUMAN).drop_chip(copy, col)
            value = minimax(game,copy,depth-1, True)[1]
            if value < bestValue:
                bestValue = value
                column = col
        return column, bestValue
