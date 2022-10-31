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

rows_message = """
Enter no. of rows (minimum 4):
"""

def intInput(a, b, msg):
    while True:
        try:
            ch = int(input(msg))
            while ch < a or ch > b:
                print("\nPlease enter a valid choice")
                sleep(2)
                clear()
                ch = int(input(msg))
            # valid choice 
            return ch
        except:
            print("\nPlease enter a valid choice")
            sleep(2)
            clear()

def clear():
    if name == "nt":
        _ = system('cls')
    else:
        _ = system('clear')


def check_move(board, turn, col, pop):
    # implement your function here
    return True

def apply_move(board, turn, col, pop):
    # implement your function here
    return board.copy()

def check_victory(board, who_played):
    # implement your function here
    return -1

def computer_move(board, turn, level):
    # implement your function here
    return (0,False)
    
def display_board(board):
    # implement your function here
    print("\n Current Board:")
    for i in range (0,len(board),7):
            print(board[i:i+7])
    pass

def menu():
    # implement your function here
    print("Welcome!")
    choice = intInput(1,3, choices_message)
    rows = intInput(4,float('inf'),rows_message)
    board = [0] * 7 * rows
    display_board(board)
    pass

if __name__ == "__main__":
    menu()




    
