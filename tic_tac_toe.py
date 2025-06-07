# Display current state of the board.
def display_board(board):
    print('\n')
    print(f' {board[1]} | {board[2]} | {board[3]}')
    print('---|---|---')
    print(f' {board[4]} | {board[5]} | {board[6]}')
    print('---|---|---')
    print(f' {board[7]} | {board[8]} | {board[9]}')
    print('\n')
    
# Placeholder '#' used so players can use positions 1-9 instead of 0-8.
board = ['#','1','2','3','4','5','6','7','8','9'] 

# Handle initial player symbol selection
def player_input():
    symbol = input("What will it be, X's or O's?: ").upper() # Accept X or O, case-insensitive 

    while symbol not in [ 'X', 'O']: # Input validation 
        print("Haven't you played Tic Tac Toe before? Just pick one bud.")
        symbol = input("What will it be, X's or O's?: ").upper()
    # Returing a tuple of (player1_symbol, player2_symbol)
    if symbol == 'X': 
        return ('X', 'O')
    else:
        return ('O', 'X')
# Prompt player to choose a position and update the board.    
def player_marker(board,player_symbol):
    valid = False
    valid_choice = range(1,10)
    valid_range = False
    
    while not valid:
        position = input("Use 1-9 to mark your position, bud: ")

        # Validate the input is a digit.
        if not position.isdigit():
            print('Brother, its Tic-Tac-Toe, not Rocket Surgery. Pick a spot using NUMBERS 1-9.')
            continue
        
        position = int(position) 
        
        # Validate position is in range
        if position not in valid_choice:
            print('1-9, man. 1-9')
            continue
            
        # Validate position position isn't already taken
        if board[position] in ['X', 'O']:
            print('Seats taken, Forest. Try again.')
            continue
        # All checks pass- update the board
        else:
            print('Good move, chucklenuts.')
            board[position] = player_symbol
            display_board(board)
            valid = True
# Checks if either player has won
def check_win(board,symbol): 
    win_combo = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [1,4,7],
    [2,5,8],
    [3,6,9],
    [1,5,9],
    [3,5,7]
    ]
    for combo in win_combo:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == symbol:
            return True
    return False
# checks if board is full (tie game)
def tie_check(board):
    return all(space in ['X','O'] for space in board[1:])

# Main game loop
def playgame():
    # Reset board and player symbols
    board = ['#','1','2','3','4','5','6','7','8','9']
    player1_symbol, player2_symbol = player_input()
    current_player = 'player_1'
    current_symbol = player1_symbol
    game_active = True

    while game_active:
        display_board(board)
        player_marker(board, current_symbol)
        # Checks for wins of ties
        if check_win(board, current_symbol):
            print(f'Congrats,{current_player}, you are now the unofficial Tic Tac Toe World Championship..or something like that.')
            game_active = False
        elif tie_check(board):
            print(f"Well, this is awkward.. it's a tie. ")
            game_active = False
        else:
        # Switch turns
            if current_player == 'player_1':
                current_player = 'player_2'
                current_symbol = player2_symbol
            else:
                current_player = 'player_1'
                current_symbol = player1_symbol
# Relay loop. 
while True:
    playgame()
    again = input('Wanna run it back? (y/n): ').lower()
    if again != 'y':
        print("Later, legend. Thanks for playing.")
        break
