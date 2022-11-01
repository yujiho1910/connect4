import random
import math
from time import sleep
from os import system, name

choices_message = """
Choose your options:
1) Player vs Computer (Easy)
2) Player vs Computer (Difficult)
3) Player vs Player

"""

def intInput(a, b, msg):
    while True:
        try:
            ch = int(input(msg))
            while ch < a or ch > b:
                print("\nPlease enter a valid choice")
                sleep(1)
                clear()
                ch = int(input(msg))
            # valid choice 
            return ch
        except:
            print("\nPlease enter a valid choice")
            sleep(1)
            clear()

def clear():
    if name == "nt":
        _ = system('cls')
    else:
        _ = system('clear')

def board1Dto2D(board):
    res = []
    n = len(board)
    r = n // 7
    for i in range(r-1, -1, -1):
        res.append([])
        for j in range(7):
            res[r-1-i].append(board[7*i + j])
    
    return res

def board2Dto1D(board):
    res = []
    for i in range(len(board)-1, -1, -1):
        for j in range(len(board[0])):
            res.append(board[i][j])

    return res

def check_move(board, turn, col, pop):
    # implement your function here
    board2 = board1Dto2D(board)
    display_board(board)
    if pop:
        if board2[-1][col] == turn:
            return True 
        else:
            return False 
    else:
        if board2[0][col] == 0:
            return True
        else:
            return False


def apply_move(board, turn, col, pop):
    # implement your function here
    board2 = board1Dto2D(board)
    if check_move(board, turn, col, pop):
        if pop:
            row = len(board2) - 1
            while row >= 0 and board2[row][col]:
                board2[row][col] = board2[row-1][col]
                row -= 1
        else:
            row = 0
            while row < len(board2) and board2[row][col] == 0:
                row += 1
            board2[row-1][col] = turn 
    board = board2Dto1D(board2)
    return board.copy()

def check_victory(board, who_played):
    # implement your function here
    board2 = board1Dto2D(board)
    return -1

def computer_move(board, turn, level):
    # implement your function here
    board2 = board1Dto2D(board)
    return (0,False)
    
def display_board(board):
    # implement your function here
    board2 = board1Dto2D(board)
    for i in board2:
        print(i)
    pass

def menu():
    # implement your function here
    clear()
    print("Welcome!")
    sleep(1)
    choice = intInput(1,3, choices_message)
    pass

if __name__ == "__main__":
    menu()




    
