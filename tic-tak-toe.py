# import random
# board = ["-", "-", "-",
#          "-", "-", "-", 
#          "-", "-", "-"]
# currentPlayer = "X" 
# secondPlayer = "O"
# winner = None
# gameRunning = True


# #printing the game board
# def printBoard(board):
#     print(board[0] + " | " + board[1] + " | " + board[2])
#     print("---------")
#     print(board[3] + " | " + board[4] + " | " + board[5])
#     print("---------")
#     print(board[6] + " | " + board[7] + " | " + board[8])
# printBoard(board)   
    

# #take player input 
# def playerInput(board):
#     inp = int(input("Enter a number 1-9: "))
#     if inp >= 1 and inp <= 9 and board[inp-1] == "-":
#         board[inp-1] = currentPlayer
#     else:
#         print("Oops player is already in that spot!")
        
# #check for win or tie
# def chackHorizontle(board):
#     global winner
#     if board[0] == board[1] == board[2] and board[1] != "-":
#         winner = board[0]
#         return True
#     elif board[3] == board[4] == board[5] and board[3] != "-":
#         winner = board[3]
#         return True
#     elif board[6] == board[7] == board[8] and board[6] != "-": 
#         winner = board[6]
#         return True
        
# def checkRow(board):
#     global winner 
#     if board[0] == board[3] == board[6] and board [0] != "-":
#         winner = board[0]
#         return True 
    
#     elif board[1] == board[4] == board[7] and board[1] != "-":
#         winner = board[1]
#         return True
    
#     elif board[2] == board[5] == board[8] and board[2] != "-":
#         winner = board[2]
#         return True

# def checkDiag(board):
#     global winner
#     if board[0] == board[4] == board[8] and board[0] == "-":
#         winner = board[0]
#         return True
    
#     elif board[2] == board[4] == board[6] and board[2] != "-":
#         winner = board[2]
#         return True
    
    
# def checkTie(board):
#     global gameRunning
#     if "-" not in board:
#         printBoard(board)
#         print("it's a Tie!")
#         gameRunning = False
        
# def checkWin():
#     if checkDiag(board) or chackHorizontle(board) or checkRow(board):
#         print(f"the winner is {winner}" ) 
#         quit()
         
    
    
# #switch the player 

# def switchPlayer():
#     global currentPlayer
#     if currentPlayer == "X":
#         currentPlayer = "O"
#     else:
#         currentPlayer = "X"
        
        
# #computer
# def computer(board):
#     while currentPlayer == "O":
#         possition = random.randint(0,8)
#         if board[possition] == "-":
#             board[possition] ="O"
#             switchPlayer()
        
# #check for win or tie again
# while gameRunning:
#     printBoard(board)
#     playerInput(board)
#     checkWin()
#     checkTie(board)
#     switchPlayer()
#     computer(board)
#     checkWin()
#     checkTie(board)
    
import random


board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]
currentPlayer = "X"
winner = None
gameRunning = True

# game board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])


# take player input
def playerInput(board):
    inp = int(input("Select a spot 1-9: "))
    if board[inp-1] == "-":
        board[inp-1] = currentPlayer
    else:
        print("Oops player is already at that spot.")


# check for win or tie
def checkHorizontle(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[3]
        return True


def checkDiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[4] != "-":
        winner = board[2]
        return True


def checkIfWin(board):
    global gameRunning
    if checkHorizontle(board):
        printBoard(board)
        print(f"The winner is {winner}!")
        gameRunning = False

    elif checkRow(board):
        printBoard(board)
        print(f"The winner is {winner}!")
        gameRunning = False

    elif checkDiag(board):
        printBoard(board)
        print(f"The winner is {winner}!")
        gameRunning = False


def checkIfTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("It is a tie!")
        gameRunning = False


# switch player
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"


def computer(board):
    while currentPlayer == "O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            switchPlayer()


while gameRunning:
    printBoard(board)
    playerInput(board)
    checkIfWin(board)
    checkIfTie(board)
    switchPlayer()
    computer(board)
    checkIfWin(board)
    checkIfTie(board)
