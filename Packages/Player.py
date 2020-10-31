class Player:
    """Creates a Tic-tac-toe player profile.

    Args:
        player_name (str): Contains user-input string of the player's name.
        symbol (str): Player's marker to be inserted into the gameboard.
        max_box (int): maximum number of tiles on the gameboard, used for 
                      error detection.
    
    Attributes:
        player_name (str): Contains user-input string of the player's name.
        mark (str): Player's marker to be inserted into the gameboard.
        max_box (int): maximum number of tiles on the gameboard, used for 
                      error detection.

    """

    def __init__(self, player_name, symbol, max_box):
        #Creates a new player profile
        self.pname = player_name
        self.mark = symbol
        self.max_box = max_box

    def play(self, board, box_num, turn_number):
        """Modifies the gameboard according to the player's input

        Args:
            board (list): 2D list containing all elements of the board
            box_num (int): Player input of the box they wish to mark
            turn_number (int): Incremental variable that will increase by 1
                              if successful play is made

        Returns:
            Unsuccessful play: Integer corresponding to external dict
            containing rejection messages.
            Successful play: List containing updated gameboard matrix,
            row and column of specified box, and the incremented turn number.

        """

        if box_num > self.max_box:
            return 1

        row = (box_num - 1)//(len(board))
        col = (box_num - 1)%len(board)

        if type(board[row][col]) is str:
            return 2
        
        board[row][col] = self.mark
        turn_number += 1
        return [board, row, col, turn_number]