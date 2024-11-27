import random
board=['_']*10
user='X'
computer='O'

def display_board(board):
    print(f'{board[1]} | {board[2]} | {board[3]} ' )
    print(f'{board[4]} | {board[5]} | {board[6]} ' )
    print(f'{board[7]} | {board[8]} | {board[9]} ' )


def win():
    if board[1]==board[2]==board[3] and board[1]!='_':
        return True
    elif board[4]==board[5]==board[6] and board[4]!='_' :
        return True
    elif board[7]==board[8]==board[9] and board[7]!='_' :   
        return True
    elif board[1]==board[4]==board[7] and board[1]!='_' :
        return True
    elif board[2]==board[5]==board[8] and board[2]!='_' :
        return True
    elif board[3]==board[6]==board[9] and board[3]!='_' :
        return True
    elif board[1]==board[5]==board[9] and board[1]!='_' :
        return True
    elif board[7]==board[5]==board[3] and board[7]!='_' :
        return True
    else:
        return False
    
def user_play(user):
    while True:
        try:
            user_input=int(input('Enter a number between 1-9: '))
            if board[user_input]=='_':
                board[user_input]=user
                break
            else:
                print("position taken")
        except (ValueError):
            print("Invalid input enter a number between 1-9.")

def computer_play(computer):
    while True:
        computer_input = random.randint(1, 9)
        if board[computer_input] == '_':
            board[computer_input] = computer
            break


def play_game():
    game_over=False
    while not game_over:
        display_board(board)

        user_play(user)
        if win():
            display_board(board)
            print("You win!")
            game_over=True
            break

        if '_' not in board[1:]:
            display_board(board)
            print("It's a tie!")
            game_over=True
            break

        computer_play(computer)
        if win():
            display_board(board)
            print("Computer wins!")
            game_over=True
            break

        if '_' not in board[1:]:
            display_board(board)
            print("It's a tie!")
            game_over=True
play_game()