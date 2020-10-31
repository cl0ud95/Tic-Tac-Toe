class GameBoard:
    """Creates a 2D list for the game of Tic-tac-toe

    Args:
        board_length (int): User-specified integer that must be more than 2.
                           Denotes length of square board.

    Attributes:
        matrix (list): 2D list of length `board_length`
        max_box (int): Total number of boxes in board
        length (int): Length of board
        turn_number (int): Number of successful plays made on the board

    """

    def __init__(self, board_length):
        #Creates a 2D list of a specified dimension
        board_array = []
        for i in range(board_length):
            start_box = 1 + i*board_length
            end_box = (1 + i)*board_length + 1
            board_array.append([n for n in range(start_box, end_box)])
        self.matrix = board_array
        self.max_box = board_length**2
        self.length = board_length
        self.turn_number = 0

    def print_board(self):
        """Prints out the board in stdout for user to visualise

        Example: 1 | 2 | 3
                -----------
                 4 | 5 | 6
                -----------
                 7 | 8 | 9
        """

        printed_board = ''
        for i in range(self.length):
            printed_board += ' | '.join(map(str, self.matrix[i])) + '\n'
            if i != self.length - 1:
                printed_board += '-'*(4*(self.length) - 1) + '\n'
        
        print(printed_board)

    def stop_game(self, row, col, player_name):
        """Checks the board matrix for a game-ending condition
           after play is made

        Args:
            row (int): Index of the parent array containing box
            col (int): Index of the inner array containing box
            player_name (str): Name of player making the move

        Returns:
            If all boxes are filled: String denoting a draw condition
            If player get 3 consecutive marks in a row: String announcing the
                winning player's name
            Else: Return False
        """

        stop_conditions = {
            1:'All boxes have been filled, the game ends in a draw',
            2:f'Congratulations {player_name}! You have won!'
            }

        def check_win(input_list):
            #Checks for 3 consecutive same elements in a list
            for i in range(len(input_list) - 2):
                if input_list[i] == input_list[i + 1] == input_list[i + 2]:
                    return True
            return False    
        
        #Condition 1: If all cells have been filled, return draw condition
        if self.turn_number == self.max_box:
            return stop_conditions[1]

        N = row - 2
        S = row + 2
        W = col - 2
        E = col + 2

        board_index = [n for n in range(self.length)]

        #Condition 2: Checks the horizontal, vertical and diagonals using a list of up to length 5, with the specified cell in the middle.
        #This represents the 'winning range' of the player. If any list contains 3 consecutive same elements, a win condition is returned. 
        if check_win([self.matrix[row][i] if i in board_index else '-' for i in range(W, E + 1)]):    #Checks horizontal
            return stop_conditions[2]
        elif check_win([self.matrix[i][col] if i in board_index else '-' for i in range(N, S + 1)]):  #Checks vertical
            return stop_conditions[2]
        elif check_win([self.matrix[i][j] if (i in board_index and j in board_index) else '-' for i,j in zip(range(N, S + 1), range(W, E + 1))]):
            return stop_conditions[2]    #Checks left-to-right diagonal
        elif check_win([self.matrix[i][j] if (i in board_index and j in board_index) else '-' for i,j in zip(range(N, S + 1), range(E, W - 1, -1))]):
            return stop_conditions[2]    #Checks right-to-left diagonal

        return False