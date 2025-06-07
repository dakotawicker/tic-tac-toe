#Display Board
def display_board(board):
    print('\n')
    print(f' {board[1]} | {board[2]} | {board[3]}')
    print('---|---|---')
    print(f' {board[4]} | {board[5]} | {board[6]}')
    print('---|---|---')
    print(f' {board[7]} | {board[8]} | {board[9]}')
    print('\n')

board = ['#','1','2','3','4','5','6','7','8','9'] 
# I used '#' as a place holder so when players choose an index they can pick 1-9, instead of 0-8. Hopefully making more
#  user friendly.

def player_input():
    symbol = input("What will it be, X's or O's?: ").upper() # .upper() is to insure the player can pick x or X/o or O

    while symbol not in [ 'X', 'O']: #input validation 
        print("Haven't you played Tic Tac Toe before? Just pick one bud.")
        symbol = input("What will it be, X's or O's?: ").upper()
    
    if symbol == 'X': #returing a tuple to use in game logic later on.
        return ('X', 'O')
    else:
        return ('O', 'X')
    
def player_marker(board,player_symbol):
    valid = False
    valid_choice = range(1,10)
    valid_range = False
    
    while not valid:
        # check to see if input is a digit and if so, convert it to an int. If not, reprompt player.
        position = input("Use 1-9 ro mark your position, bud: ")
        if not position.isdigit():
            print('Brother, its Tic-Tac-Toe, not Rocket Surgery. Pick a spot using NUMBERS 1-9.')
            continue
        # store position's int value
        position = int(position) 
        # now check if position int value is in the corrent range to pick a valid index for their board position.
        if position not in valid_choice:
            print('1-9, man. 1-9')
            continue
        # check if the position is taken. if so, reprompt player.
        if board[position] in ['X', 'O']:
            print('Seats taken, Forest. Try again.')
            continue
        # if everything checks out, update board.
        else:
            print('Good move, chucklenuts.')
            board[position] = player_symbol
            display_board(board)
            valid = True





        
        

