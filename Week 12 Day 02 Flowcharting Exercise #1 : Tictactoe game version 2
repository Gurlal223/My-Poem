import random
def checkWinner(board):
    result = "None"
    filledCount = 0
    if board[1] != " " and board[1] == board[2] and board[2] == board[3]:
        result = board[1]
    if board[4] != " " and board[4] == board[5] and board[5] == board[6]:
        result = board[4]
    if board[7] != " " and board[7] == board[8] and board[8] == board[9]:
        result = board[7]
    if board[1] != " " and board[1] == board[4] and board[4] == board[7]:
        result = board[1]
    if board[2] != " " and board[2] == board[5] and board[5] == board[8]:
        result = board[2]
    if board[3] != " " and board[3] == board[6] and board[6] == board[9]:
        result = board[3]
    if board[1] != " " and board[1] == board[5] and board[5] == board[9]:
        result = board[1]
    if board[3] != " " and board[3] == board[5] and board[5] == board[7]:
        result = board[3]
    for k in range(1, 9 + 1, 1):
        if board[k] != " ":
            filledCount = filledCount + 1
    if result == "None" and filledCount == 9:
        result = "Draw"
    
    return result

def computerMove(board):
    valid = False
    while valid == False:
        compMove = int(random.random() * 9) + 1
        if board[compMove] == " ":
            valid = True
        else:
            valid = False
    
    return compMove

def displayBoard(board):
    print(board[1] + " | " + board[2] + " | " + board[3])
    print("-+-+-")
    print(board[4] + " | " + board[5] + " | " + board[6])
    print("-+-+-")
    print(board[7] + " | " + board[8] + " | " + board[9])

# Main
random.seed()   #Prepare random number generator

print("Hello, dear user! I am Flowy, your friendly game master! Today, we'll play a game of Tic-Tac-Toe. Are you ready- oh, what's your name?")
name = input()
print("Wonderful name, " + name + "! Let's start the game, shall we?")
board = [""] * (10)

for i in range(1, 9 + 1, 1):
    board[i] = " "
gameOver = False
winner = "None"
r = int(random.random() * 2)
if r == 0:
    currentPlayer = "O"
else:
    currentPlayer = "X"
while gameOver == False:
    displayBoard(board)
    if currentPlayer == "O":
        validMove = False
        while validMove == False:
            print("Dear user, it's your turn! Choose a cell (1 - 9):")
            humanMove = int(input())
            if humanMove >= 1 and humanMove <= 9:
                if board[humanMove] == " ":
                    validMove = True
                else:
                    print("Oops, that space is occupied! Try again.")
            else:
                print("Oops, that's an invalid input! You can only enter from 1 - 9. Try again!")
        board[humanMove] = "O"
    else:
        print("Computer, it's your turn! Choose a cell (1 - 9):")
        compMove = computerMove(board)
        board[compMove] = "X"
    winner = checkWinner(board)
    if winner != "None":
        gameOver = True
    else:
        if currentPlayer == "O":
            currentPlayer = "X"
        else:
            currentPlayer = "O"
displayBoard(board)
if winner == "O":
    print("Game Over! Congratulations, Dear User. You win!")
else:
    if winner == "X":
        print("Game Over! Congratulations. Computer wins!")
    else:
        print("Game Over! It's a tie! Congratulations to the players!")
