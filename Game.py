"""Creates a game of Tic-tac-toe for 2 players with a customizable board size.

This program runs a game of Tic-Tac-Toe with a variable sized board
whose length can be decided by the player.

2 players will take turns putting 'X' or 'O' on the board until
1. All tiles are filled, in which case the game ends in a draw.
2. A player acheives 3 consecutive marks in any direction
   (1 horizontal, 1 vertical and 2 diagonals)


"""

from Packages.Player import Player
from Packages.GameBoard import GameBoard

if __name__ == '__main__':

    #This function runs the steps of a typical round
    def player_turn(player, player_input, board):
        bad_output = {1:'Box is not in the game board, please try again',
            2:'Box has already been filled, please try again'}

        #Here, the player makes his mark on the board,
        #and the program detects if there are any wrong inputs
        output = player.play(board.matrix, player_input, board.turn_number)

        if type(output) is int:
            bad_turn = True
            while bad_turn:
                output = player.play(board.matrix,
                        input(bad_output[output]),
                        board.turn_number)
                if type(output) is list:
                    bad_turn = False

        #With a valid input, the program updates the turn number
        #And checks for an end_game condition
        board.turn_number = output[3]
        board.matrix = output[0]
        board.print_board()
        end_game = board.stop_game(output[1], output[2], player.pname)
        if end_game:
            return end_game
        else:
            return False

    #Setting up the game with board size and player names
    wrong_entry = True
    size = int(input('Please enter the size of your board \n'))
    while wrong_entry:

        if size >= 3:
            board = GameBoard(size)
            wrong_entry = False

        if wrong_entry:
            entry = input('Please enter an integer greater than or equal to 3')

    print(f'{board.length}x{board.length} board created')
    player_1 = Player(input('Enter Player 1 name \n'), 'X', board.max_box)
    player_2 = Player(input('Enter Player 2 name \n'), 'O', board.max_box)

    #Game starts
    board.print_board()
    while True:
        
        end_game = player_turn(player_1,
                int(input(f'{player_1.pname}, choose a box to place a \'{player_1.mark}\' into \n')),
                board)
        if end_game:
            print(end_game)
            break

        end_game = player_turn(player_2,
                int(input(f'{player_2.pname}, choose a box to place a \'{player_2.mark}\' into \n')),
                board)
        if end_game:
            print(end_game)
            break