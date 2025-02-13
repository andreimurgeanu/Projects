#Print board
from IPython.display import clear_output

def display_board(board):
    clear_output()
    print('\n '+board[7]+' | '+board[8]+' | '+board[9]+' \n'+'-----------\n'+' '+board[4]+' | '+board[5]+' | '+board[6]+' \n'+'-----------\n'+' '+board[1]+' | '+board[2]+' | '+board[3]+' ')    


#Assign X or O to players
def player_input():
    acceptableValues=['X','O','x','o']
    inputMarker=''
    while inputMarker not in acceptableValues:
        inputMarker=input('Please select your marker(X or O):')
        
        if inputMarker in acceptableValues:
            print("Your marker is:",inputMarker.upper())

#Mark position
def place_marker(board, marker, position):
    board[position]=marker


#Check win
def win_check(board, mark):
    if board[7]==board[8]==board[9]==mark or board[4]==board[5]==board[6]==mark or board[1]==board[2]==board[3]==mark or board[1]==board[4]==board[7]==mark or board[2]==board[5]==board[8]==mark or board[3]==board[6]==board[9]==mark or board[7]==board[5]==board[3]==mark or board[1]==board[5]==board[9]==mark:
        return True


#Which player goes first?
import random

def choose_first():
    a=1
    b=100
    player1=1
    player2=1
    while player1==player2:
        player1=random.randint(a,b)
        player2=random.randint(a,b)
    if player1>player2:
        return "Player1 will go first"
    else:
        return "Player2 will go first"
choose_first()

#Check if the space is open
def space_check(board, position):
    if board[position]==' ':
        return True
    else:
        return False
space_check(test_board,1)

#Check if the board is full
def full_board_check(board):
    for i in range(1,10):
        if board[i]==" ":
            return False
    return True
full_board_check(test_board)

#Ask player for position. Check if it is open
def player_choice(board):
    inputPosition=int(input("Please enter position(1 to 9): "))
    print(inputPosition)

    while space_check(board,inputPosition)==False:
        inputPosition=int(input("Please enter position(1 to 9): "))
        print(inputPosition)
    if space_check(board,inputPosition)==True:
        return inputPosition

#Want to play again?
def replay():
    inputReplay=input("Do you want to play again?(Yes or No)")
    if inputReplay=="Yes" or inputReplay=='yes':
        return True
    else:
        return False
replay()


#Main game
print('Welcome to Tic Tac Toe!')

#while True:
    # Set the game up here
    #pass

    #while game_on:
        #Player 1 Turn
        
        
        # Player2's turn.
            
            #pass

    #if not replay():
        #break
while True:        
    empty_board=['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
        
    display_board(empty_board)
    #player_input()
    if choose_first()=="Player1 will go first":
        print("Player 1 will go first\n")
        while full_board_check(empty_board)!=True:
            place_marker(empty_board,"X",player_choice(empty_board))
            display_board(empty_board)
            
            if full_board_check(empty_board)==True:
                print("Tie")
                break
    
            if win_check(empty_board,"X")==True:
                print("!!! X won the game!!!")
                break
    
            place_marker(empty_board,"O",player_choice(empty_board))
            display_board(empty_board)
    
            if win_check(empty_board,"O")==True:
                print("!!! O won the game!!!")
                break

    else:
        print("Player 2 will go first\n")
        while full_board_check(empty_board)==False:
            place_marker(empty_board,"O",player_choice(empty_board))
            display_board(empty_board)
    
            if win_check(empty_board,"O")==True:
                print("!!! O won the game!!!")
                break
    
            place_marker(empty_board,"X",player_choice(empty_board))
            display_board(empty_board)
    
            if win_check(empty_board,"X")==True:
                print("!!! X won the game!!!")
                break
    if not replay():
        break
