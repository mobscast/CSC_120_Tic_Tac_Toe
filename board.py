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
        row = int(input("Enter the row number that you want play [1-3]")) - 1
        if board[row][col] == "X" or board[row][col] == "O":
            print("Space has already been taken. Please choose another space.")
        else:
            board[row][col] = player
            playFlag = False


# Play
printboard()
while win == False:
    turn(player1)
    printboard()

    turn(player2)
    printboard()