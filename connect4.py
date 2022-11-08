import random
from time import sleep
from os import system, name


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
    new = board[:]
    if pop:
        if rows == 1:
            new[col] = 0
        else:
            row = 0
            while row < rows and new[7*row + col]:
                new[7*row + col] =  new[7*(row+1) + col]
                row += 1
    else:
        row = rows - 1
        while row >= 0 and new[7*row + col] == 0:
            row -= 1
        new[7*(row+1)+col] = turn 
    return new.copy()

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
            j = random.randint(0, cols-1)
            pop = random.randint(0, 1)
            if pop == 0:
                if check_move(board, turn, j, True):
                    return (j, True)
            else:
                if check_move(board, turn, j, False):
                    return (j, False)

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
            j = random.randint(0, cols-1)
            pop = random.randint(0, 1)
            if pop == 0:
                if check_move(board, turn, j, True):
                    board_tmp = apply_move(board, turn, j, True)
                    if not check_victory(board_tmp, 1):
                        return (j, True)
            else:
                if check_move(board, turn, j, False):
                    return (j, False)

def display_board(board):
    count = 0
    s = ""
    i = 0
    temp = ""
    while i < len(board):
        if board[i] == 0:
            temp += "[ ]"
        else:
            temp += "[" + str(board[i]) + "]" 
        count += 1 
        i += 1
        if count == 7:
            if s == "":
                s = '\n' + temp
            else:
                s = '\n' + temp + s
            count = 0
            temp = ""
    print(s)
    pass

def menu():
    clear()
    print("Welcome to connect4!")
    sleep(1)
    print("Choose a game mode!")
    message1 = "a) Play against Computer (Level 1)" + "\nb) Play against Computer (Level 2)" + "\nc) Play with another friend (2 Player)\n\n"
    message2 = "Enter no. of rows (1-10):"
    message3 = "Which column would you like to place your piece? (1-7):"
    message4 = "Would you like to pop your disc? \n0: No \n1:Yes\n"
    clear()
    choice = input(message1)
    while choice != 'a' and choice != 'b' and choice != 'c':
        clear()
        print("Key in a valid choice")
        sleep(1)
        choice = input(message1)
    clear()
    while True:
        rows = input(message2)
        if rows.isdigit():
            rows = int(rows)
            if 1<=rows<=10:
                break
        print("Key in a valid choice!")

    size = rows * 7
    board = [0] * size 
    turn = 1

    while not check_victory(board, turn+1):
        turn = (turn + 1) % 2
        clear()
        display_board(board)
        if turn == 1 and choice != 'c':
            if choice == 'a':
                col, pop = computer_move(board, turn+1, 1)
                board = apply_move(board, turn+1, col, pop)
                clear()
                display_board(board)
                if pop:
                    print("Computer popped at column", col+1)
                else:
                    print("Computer added a disc at column", col+1)
                input("\nPress enter to continue")
            elif choice == 'b':
                col, pop = computer_move(board, turn+1, 2)
                board = apply_move(board, turn+1, col, pop)
                clear()
                display_board(board)
                if pop:
                    print("Computer popped at column", col+1)
                else:
                    print("Computer added a disc at column", col+1)
                input("\nEnter to continue")
        else:
            if choice == 'c':
                print("Player " + str(turn+1) + "'s turn ")
            else:
                print("Player's turn ")
            
            while True:
                while True:
                    col = input(message3)
                    if col.isdigit():
                        col = int(col)
                        if 1<=col<=7:
                            break
                    print("Key in a valid choice!")
                pop = 0
                if board[col-1] == turn+1:
                    while True:
                        pop = input(message4)
                        if pop.isdigit():
                            pop = int(pop)
                            if 0<=pop<=1:
                                break
                        print("Key in a valid choice!")
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
    if choice != 'c':
        if check_victory(board, turn+1) == 1:
            print("Player wins!")
        else:
            print("Computer wins")
    else:
        print("Player " + str(check_victory(board, turn+1)) + " win!")
    print("\nQuitting the program...")

    pass

if __name__ == "__main__":
    menu()

