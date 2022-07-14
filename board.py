from math import fabs
from turtle import back


board = [['-','-','-']
        ,['-','-','-']
        ,['-','-','-']]

player1 = 'X'
player2 = 'O'
turnNum = 0
win = False

# Prints the board
def printboard():
    print(board[0])
    print(board[1])
    print(board[2])

# Gets the Column and Row that the player wants, checks to see if it has already been played and plays it.
def turn(player):
    print(player + "'s turn")
    playFlag = True
    while playFlag:
        col = int(input("Enter the column number that you want to play [1-3]")) - 1
        while col < 0 or col >= 3:
            print("Invalid column number")
            col = int(input("Enter the column number that you want to play [1-3]")) - 1
        row = int(input("Enter the row number that you want play [1-3]")) - 1
        while row < 0 or row >= 3:
            print("Invalid row number")
            row = int(input("Enter the row number that you want to play [1-3]")) - 1
        if board[row][col] == "X" or board[row][col] == "O":
            print("Space has already been taken. Please choose another space.")
        else:
            board[row][col] = player
            playFlag = False

# Checks all possible win chances and sets 
def checkWin(player):
    for i in range(0, 3):
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            print(player, "Wins!")
            winFlag = True
            break
        elif board[0][i] == player and board[1][i] == player and board[2][i] == player:
            print(player, "Wins!")
            winFlag = True
            break
        elif board[0][0] == player and board[1][1] == player and board[2][2] == player:
            print(player, "Wins!")
            winFlag = True
            break
        elif board[0][2] == player and board[1][1] == player and board[2][0] == player:
            print(player, "Wins!")
            winFlag = True
            break
        else:
            winFlag = False
    return winFlag

# Play
printboard()
while win == False:
    turn(player1)
    turnNum += 1
    printboard()
    if checkWin(player1):
        win = True
        break
    if turnNum == 9:
        print("Draw, Game Over!!")
        win = True
        break

    turn(player2)
    turnNum += 1
    printboard()
    if checkWin(player2):
        win = True
        break