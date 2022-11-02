import random
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
            if len(board2) == 1:
                board2[0][col] = 0
            else:
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
    board2 = board1Dto2D(board)
    row = len(board2)
    col = len(board2[0])

    if helper(board2,1,row,col) and who_played==2:
        return 1
    
    elif helper(board2,2,row,col) and who_played==1:
        return 2
    
    elif helper(board2,who_played,row,col):
        return who_played
    
    return 0

def helper(board2, who_played, row, col):
    def checkRow(i,j):
        if 0<=i<row and 0<=j<col and board2[i][j]==who_played:
            return 1+checkRow(i,j+1)
        return 0

    def checkCol(i,j):
        if 0<=i<row and 0<=j<col and board2[i][j]==who_played:
            return 1+checkCol(i+1,j)
        return 0
    
    def checkDownslope(i,j):
        if 0<=i<row and 0<=j<col and board2[i][j]==who_played:
            return 1+checkDownslope(i+1,j+1)
        return 0
    
    def checkUpslope(i,j):
        if 0<=i<row and 0<=j<col and board2[i][j]==who_played:
            return 1+checkUpslope(i+1,j-1)
        return 0
    
    for i in range(row):
        for j in range(col):
            if checkRow(i,j)>=4 or checkCol(i,j)>=4 or checkDownslope(i,j)>=4 or checkUpslope(i,j)>=4:
                return 1
    
    return 0

def computer_move(board, turn, level):
    # implement your function here
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
    # implement your function here
    board2 = board1Dto2D(board)
    for i in board2:
        for j in i:
            if j == 0:
                print("[ ]", end="")
            elif j == 1:
                print("[O]", end="")
            else:
                print("[X]", end="")
        print()
    pass

def menu():
    # implement your function here
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
                icon = "(O)"
                if choice == 3:
                    if turn == 1:
                        icon = "(X)"
                    print("Player " + str(turn+1) + "'s turn " + icon)
                else:
                    print("It's your turn " + icon)
                
                while True:
                    col = intInput(1,7, textwrap.dedent(col_message))
                    pop = 0
                    if board[col-1] == turn+1:
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




    
