"""
Tic Tac Toe Player
"""

import math
import copy
import random

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    countX = 0
    countO = 0
    for b in board:
        for i in range(3):
            if b[i] == X:
                countX += 1
            elif b[i] == O:
                countO += 1
    if countX == 0 or countX == countO:
        return X
    elif countX > countO:
        return O    


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    """
    This is the bug I don't know why but if I remove this part then in third if there is winner or not but it doesn't check it so additionally add it for third row
    """
    if board[2][0] == board[2][1] and board[2][1] == board[2][2]:
        return board[2][0]

    
    """
    Check horizontally and vertically
    """
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
            return board[i][0]
        if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
            return board[0][i]

    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return board[0][0]
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return board[0][2]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is None:
        for b in board:
            for i in range(3):
                if b[i] is None:
                    return False
        return True
    else:
        return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        win = winner(board)
        if win == X:
            return 1
        elif win == O:
            return -1
        else:
            return 0

def minimax(board):
    player1 = player(board)
    flag = True
    for i in range(3):
        for j in range(3):
            if board[i][j] is not None:
                flag = False
                break
    if flag:
        return (random.randint(0,2),random.randint(0,2))
    
    if player1 == X:
        return maxi(board)
    elif player1 == O:
        return mini(board)

def min_value(board):
    if terminal(board):
        return utility(board)
    new_board = copy.deepcopy(board)
    list1 = []
    for i in range(3):
        for j in range(3):
            if new_board[i][j] is None:
                if player(new_board) == O:
                    new_board[i][j] = O
                    list1.append(max_value(new_board))
                    new_board[i][j] = None
    return min(list1)

def max_value(board):
    if terminal(board):
        return utility(board)
    new_board = copy.deepcopy(board)
    list1 = []
    for i in range(3):
        for j in range(3):
            if new_board[i][j] is None:
                if player(new_board) == X:
                    new_board[i][j] = X
                    list1.append(min_value(new_board))
                    new_board[i][j] = None
    return max(list1)
    
def mini(board):
    new_board = copy.deepcopy(board)
    list1 = []
    action1 = []
    for i in range(3):
        for j in range(3):
            if new_board[i][j] is None:
                if player(new_board) == O:
                    new_board[i][j] = O
                    list1.append(max_value(new_board))
                    action1.append((i,j))
                    new_board[i][j] = None
    return action1[list1.index(min(list1))]

def maxi(board):
    new_board = copy.deepcopy(board)
    list1 = []
    action1 = []
    for i in range(3):
        for j in range(3):
            if new_board[i][j] is None:
                if player(new_board) == X:
                    new_board[i][j] = X
                    list1.append(min_value(new_board))
                    action1.append((i,j))
                    new_board[i][j] = None 
    return action1[list1.index(max(list1))]
