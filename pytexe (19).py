import random
import os
clear = lambda: os.system('cls')

def main():
    player = 'X'
    computer = 'O'
    print ("User has", player, "and will go first...")

	while not is_draw or not has_player_won:
		get_user_move(game_board, player)
		display_board(game_board)
		print_line()
		get_computer_move(game_board, computer)
		display_board(game_board)
		print_line()
		is_draw(game_board)

    print('Thanks for playing!')
   
game_board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
        ]
def display_board(game_board):
  print (str(game_board[0][0]) + '|' + str(game_board[0][1]) + '|' + str(game_board[0][2]))
  print ('-+-+-')
  print (str(game_board[1][0]) + '|' + str(game_board[1][1]) + '|' + str(game_board[1][2]))
  print ('-+-+-')
  print (str(game_board[2][0]) + '|' + str(game_board[2][1]) + '|' + str(game_board[2][2]))
  print ('')

def print_line():
    print('=' * 20)

def get_user_move(game_board, player):
    print ("It's your turn...")
    row = int(input(('What row do you want to play (0-2)')))
    column = int(input(('What column do you want to play (0-2)')))   
    w = is_legal_move(game_board, row, column)
    while w ==1:
        row = int(input(('What row do you want to play (0-2)')))
        column = int(input(('What column do you want to play (0-2)'))) 
        w = is_legal_move(game_board, row, column)
    game_board[row][column] = player

     
def get_computer_move(game_board, computer):
    print ("Computer's turn...")
    row = random.randint(0,2)
    column = random.randint(0,2) 
    w = is_legal_move(game_board, row, column)
    while w ==1:
        row = random.randint(0,2)
        column = random.randint(0,2)
        w = is_legal_move(game_board, row, column)
    game_board[row][column] = computer

def is_legal_move(game_board, row, column):
    if row >=0 and row <= 2:
        print ("")
    else:
        print ("That is an ivalid move, Please try again.")
        return 1
    if column >=0 and column <= 2:
        print ("")
    else:
        print ("That is an ivalid move, Please try again.")
        return 1
    if game_board[row][column] == 'X' or game_board[row][column] == 'O':
        print ("That is an ivalid move, Please try again.")
        return 1
    
def is_draw(game_board):
    #Determine if a game is a draw by checking each space. Once we find at
    #least one empty spot, we can return False since it's a playable spot."""
    draw = True
    for i in range(3):
        for j in range(3):
            if game_board[i][j] == ' ':
                draw = False
    if draw:
        print ("the game is a draw")   
        
def has_player_won(game_board, symbol):
    """Check to see if the given symbol has won the game in any of the possible
       ways."""
    
    # Remember, with sequences the multiplication
    # operator repeats the value so 'X' * 3 == 'XXX'
    winner_sequence = player or computer * 3 
    
    # Check for horizontal wins
    for r in range(len(game_board)):
        row_symbols = ''
        for c in range(len(game_board[row])):
            row_symbols += game_board[row][column]
        if row_symbols == winner_sequence:
            return True
        
    # Check for vertical wins
    for c in range(len(game_board[0])):
        col_symbols = ''
        for r in range(len(game_board)):
            col_symbols += game_board[row][column]
        if col_symbols == winner_sequence:
            return True
            
    # Check for the two diagonal wins
    # Note this will only work on a square board!
    diag_symbols = ''
    anti_diag_symbols = ''
    for rc in range(len(game_board)):
        diag_symbols += game_board[rc][rc]
        anti_diag_symbols += game_board[rc][len(game_board) - 1 - rc]
    if winner_sequence in (diag_symbols, anti_diag_symbols):
        return True
    
    # If we got here, nobody won yet
    return False
while True:
    main()
    if input("Play again (y/n)\n") != "y":
        break

    
main()

