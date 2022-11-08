import random
import copy
from time import sleep
from os import system, name
import textwrap

def intInput(a, b, msg):
    while True:
        try:
            ch = int(input(msg))
            while ch < a or ch > b:
                print("\nPlease enter a valid choice")
                sleep(1)
                ch = int(input(msg))
            # valid choice 
            clear()
            return ch
        except:
            print("\nPlease enter a valid choice")
            sleep(1)

def clear():
    if name == "nt":
        _ = system('cls')
    else:
        _ = system('clear')

def check_move(board, turn, col, pop):
    # implement your function here
    rows = len(board) // 7
    if pop:
        if board[col] == turn:
            return True 
        else:
            return False 
    else:
        if board[7*(rows-1) + col] == 0:
            return True
        else:
            return False

def apply_move(board, turn, col, pop):
    # implement your function here
    rows = len(board) // 7
    board2 = copy.deepcopy(board)
    if pop:
        if rows == 1:
            board2[col] = 0
        else:
            row = 0
            while row < rows and board2[7*row + col]:
                board2[7*row + col] = board2[7*(row+1) + col]
                row += 1
    else:
        row = rows - 1
        while row >= 0 and board2[7*row + col] == 0:
            row -= 1
        board2[7*(row+1)+col] = turn 
    return board2.copy()

def check_victory(board, who_played):
    win1 = False
    win2 = False
    
    for i in range(len(board)):
        if i+3<len(board) and board[i] and board[i+1] and board[i+2] and board[i+3]:
            if board[i]==board[i+1]==board[i+2]==board[i+3]==1:
                win1=True
            if board[i]==board[i+1]==board[i+2]==board[i+3]==2:
                win2=True
        
        if i+21<len(board) and board[i] and board[i+7] and board[i+14] and board[i+21]:
            if board[i]==board[i+7]==board[i+14]==board[i+21]==1:
                win1=True
            if board[i]==board[i+7]==board[i+14]==board[i+21]==2:
                win2=True
        
        if i+24<len(board) and board[i] and board[i+8] and board[i+16] and board[i+24]:
            if board[i]==board[i+8]==board[i+16]==board[i+24]==1:
                win1 = True
            if board[i]==board[i+8]==board[i+16]==board[i+24]==2:
                win2 = True
        
        if i+18<len(board) and board[i] and board[i+6] and board[i+12] and board[i+18]:
            if board[i]==board[i+6]==board[i+12]==board[i+18]==1:
                win1 = True
            if board[i]==board[i+6]==board[i+12]==board[i+18]==2:
                win2 = True

    if win1 and who_played==2:
        return 1

    elif win2 and who_played==1:
        return 2

    elif win1 and who_played==1:
        return 1
    
    elif win2 and who_played==2:
        return 2
    
    return 0
          
def computer_move(board, turn, level):
    cols = 7
    if level == 1:
        #random inputs
        while True:
            y = random.randint(0, cols-1)
            pop = random.randint(0, 1)
            if pop == 0:
                if check_move(board, turn, y, True):
                    return (y, True)
            else:
                if check_move(board, turn, y, False):
                    return (y, False)

    elif level == 2:
        for i in range(cols):
            board_tmp = apply_move(board, turn, i, False)
            if check_victory(board_tmp, turn):
                return (i, False)

        for i in range(cols):
            board_tmp = apply_move(board, 1, i, False)
            if check_victory(board_tmp, 1):
                print((i, False))
                return (i, False)

        while True:
            y = random.randint(0, cols-1)
            pop = random.randint(0, 1)
            if pop == 0:
                if check_move(board, turn, y, True):
                    board_tmp = apply_move(board, turn, y, True)
                    if not check_victory(board_tmp, 1):
                        return (y, True)
            else:
                if check_move(board, turn, y, False):
                    return (y, False)

def display_board(board):
    count = 0
    string = ""
    i = 0
    tmpString = ""
    while i < len(board):
        if board[i] == 0:
            tmpString += "[ ]"
        else:
            tmpString += "[" + str(board[i]) + "]" 
        count += 1 
        i += 1
        if count == 7:
            if string == "":
                string = '\n' + tmpString
            else:
                string = '\n' + tmpString + string
            count = 0
            tmpString = ""
    print(string)
    pass

def menu():
    clear()
    print("Welcome!")
    sleep(1)
    
    choices_message = """
    Choose your options:
    1) Player vs Computer (Easy)
    2) Player vs Computer (Difficult)
    3) Player vs Player

    """
    rows_message = """
    Choose how many rows (1-7):
    """
    col_message = """
    Enter column to place (1-7):
    """
    pop_message = """
    Do you want to remove the bottom disc? (1 if yes, 0 if no)
    """
    while True:
        choice = intInput(1,3, textwrap.dedent(choices_message))
        rows = intInput(1,7, textwrap.dedent(rows_message))
        size = rows * 7
        board = [0] * size 
        turn = 1

        while not check_victory(board, turn+1):
            turn = (turn + 1) % 2
            clear()
            display_board(board)
            if turn == 1 and choice != 3:
                if choice == 1:
                    col, pop = computer_move(board, turn+1, 1)
                    board = apply_move(board, turn+1, col, pop)
                    clear()
                    display_board(board)
                    if pop:
                        print("Computer popped at column", col+1)
                    else:
                        print("Computer placed disc at column", col+1)
                    input("\nPress enter to continue")
                elif choice == 2:
                    col, pop = computer_move(board, turn+1, 2)
                    board = apply_move(board, turn+1, col, pop)
                    clear()
                    display_board(board)
                    if pop:
                        print("Computer popped at column", col+1)
                    else:
                        print("Computer placed disc at column", col+1)
                    input("\nPress enter to continue")
            else:
                if choice == 3:
                    print("Player " + str(turn+1) + "'s turn ")
                else:
                    print("It's your turn ")
                
                while True:
                    col = intInput(1,7, textwrap.dedent(col_message))
                    pop = 0
                    if board[col-1] == turn+1:
                        display_board(board)
                        pop = intInput(0,1, textwrap.dedent(pop_message))
                    if pop == 0:
                        if check_move(board, turn+1, col-1, False):
                            board = apply_move(board, turn+1, col-1, False)
                            break
                    else:
                        if check_move(board, turn+1, col-1, True):
                            board = apply_move(board, turn+1, col-1, True)
                            break
        clear()
        display_board(board)
        if choice != 3:
            if check_victory(board, turn+1) == 1:
                print("Player is the winner!")
            else:
                print("Computer is the winner")
        else:
            print("Player " + str(check_victory(board, turn+1)) + " is the winner!")
        print("")

        sleep(5)
        clear()
        if input("Play again?\nto quit: key in 'no'\nto play again: press any key and Enter\n").lower() == 'no':
            clear()
            print("byebye! :)")
            exit()
    pass

if __name__ == "__main__":
    menu()

