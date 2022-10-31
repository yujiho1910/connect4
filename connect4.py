import random
import math

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
    pass

def menu():
    # implement your function here
    choice = input(
"""
Welcome!
Choose your options:
1) Player vs Computer (Easy)
2) Player vs Computer (Difficult)
3) Player vs Player
"""
            )
    try:
        ch = int(choice)
        while ch < 1 or ch > 3:
            print("Please enter a valid choice")
            ch = int(input("Your choices\n" +
                        "1) Player vs Computer (Easy)\n" +
                        "2) Player vs Computer (Medium)\n" +
                        "3) Player vs Player"))

        # valid choice 
    except:
        print("Please enter a valid choice")
    pass

if __name__ == "__main__":
    menu()




    
