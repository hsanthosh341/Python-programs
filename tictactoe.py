import random

board=["-","-","-",
       "-","-","-",
       "-","-","-"]

currentplayer="X"
winner=None
gameRunning=True

#game board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])


#take player input
def playerInput(board):
    boardpostion=int(input("enter a spot 1-9: "))
    if boardpostion >=1 and boardpostion <=9 and board[boardpostion -1] =="-":
        board[boardpostion-1]=currentplayer
    else:
        print("oops! enter postion correctly")
#check for win or tie
def checkHorizontal(board):
    global winner
    if board[0] == board[1]==board[2] and board[1] != "-":
        winner=board[0]
        return True
    elif board[3] == board[4]==board[5] and board[3] != "-":
        winner=board[3]
        return True
    elif board[6] == board[7]==board[8] and board[6] != "-":
        winner=board[6]
        return True

def checkRow(board):
    global winner
    if board[0] == board[3]==board[6] and board[0] != "-":
        winner=board[0]
        return True
    elif board[1] == board[4]==board[7] and board[1] != "-":
        winner=board[1]
        return True
    elif board[2] == board[5]==board[8] and board[2] != "-":
        winner=board[2]
        return True
    
def checkDiag(board):
    global winner
    if board[0] == board[4]==board[8] and board[0] != "-":
        winner=board[0]
        return True
    elif board[2] == board[4]==board[6] and board[2] != "-":
        winner=board[2]
        return True
    
def checkTie(board):
    if "-" not in board:
        printBoard(board)
        print("It is a tie!")
        gameRunning=False

def checkWin():
    global gameRunning
    if checkDiag(board) or checkHorizontal(board) or checkRow(board):
        printBoard(board)
        print(f"The winner is {winner}")
        gameRunning=False
#switch the player
def switchPlayer():
    global currentplayer
    if currentplayer == "X":
        currentplayer="O"
    else:
        currentplayer="X"

#computer
def computer(board):
    while currentplayer == "O":
        position=random.randint(0,8)
        if board[position]=="-":
            board[position]="O"
            switchPlayer()

#check for win or tie again
while gameRunning:
    printBoard(board)
    playerInput(board)
    checkWin()
    checkTie(board)
    switchPlayer()
    computer(board)
    checkWin()
    checkTie(board)
