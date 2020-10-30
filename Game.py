### This program runs a game of Tic-Tac-Toe with a variable sized board whose length can be decided by the player.
### 2 players will take turns putting 'X' or 'O' on the board until
### 1. All tiles are filled, in which case the game ends in a draw.
### 2. A player acheives 3 consecutive marks in any direction (1 horizontal, 1 vertical and 2 diagonals)
### Have fun!

class Player:

    def __init__(self, playername, symbol, maxbox):
        #Creates a new player profile
        self.pname = playername
        self.mark = symbol
        self.maxbox = maxbox

    def play(self, board, boxnum, turnnumber):
        #Changes the value of a specified position in the board matrix to the player's mark
        if boxnum > self.maxbox:
            return 1

        row = (boxnum - 1)//(len(board))
        col = (boxnum - 1)%len(board)

        if type(board[row][col]) is str:
            return 2
        
        board[row][col] = self.mark
        turnnumber += 1
        return [board, row, col, turnnumber]

class GameBoard:

    def __init__(self, boardlength):
        #Creates a 2D list of a specified dimension
        boardarray = []
        for i in range(boardlength):
            startbox = 1 + i*boardlength
            endbox = (1 + i)*boardlength + 1
            boardarray.append([n for n in range(startbox, endbox)])
        self.matrix = boardarray
        self.maxbox = boardlength**2
        self.length = boardlength
        self.turnnumber = 0

    def printboard(self):
        #Prints out the board in stdout
        printedboard = ''
        for i in range(self.length):
            printedboard += ' | '.join(map(str, self.matrix[i])) + '\n'
            if i != self.length - 1:
                printedboard += '-'*(4*(self.length) - 1) + '\n'
        
        print(printedboard)

    def stopgame(self, row, col, playername):
        #Receives the coordinates of the last-filled cell and checks for game-ending conditions

        stopconditions = {
            1:'All boxes have been filled, the game ends in a draw',
            2:f'Congratulations {playername}! You have won!'
            }

        def checkwin(inputlist):
            #Checks for 3 consecutive same elements in a list
            for i in range(len(inputlist) - 2):
                if inputlist[i] == inputlist[i + 1] == inputlist[i + 2]:
                    return True
            return False    
        
        #Condition 1: If all cells have been filled, return draw condition
        if self.turnnumber == self.maxbox:
            return stopconditions[1]

        N = row - 2
        S = row + 2
        W = col - 2
        E = col + 2

        boardindex = [n for n in range(self.length)]

        #Condition 2: Checks the horizontal, vertical and diagonals using a list of up to length 5, with the specified cell in the middle.
        #This represents the 'winning range' of the player. If any list contains 3 consecutive same elements, a win condition is returned. 
        if checkwin([self.matrix[row][i] if i in boardindex else '-' for i in range(W, E + 1)]):    #Checks horizontal
            return stopconditions[2]
        elif checkwin([self.matrix[i][col] if i in boardindex else '-' for i in range(N, S + 1)]):  #Checks vertical
            return stopconditions[2]
        elif checkwin([self.matrix[i][j] if (i in boardindex and j in boardindex) else '-' for i,j in zip(range(N, S + 1), range(W, E + 1))]):
            return stopconditions[2]    #Checks left-to-right diagonal
        elif checkwin([self.matrix[i][j] if (i in boardindex and j in boardindex) else '-' for i,j in zip(range(N, S + 1), range(E, W - 1, -1))]):
            return stopconditions[2]    #Checks right-to-left diagonal

        return False

if __name__ == '__main__':

    #This function runs the steps of a typical round
    def playerturn(player, board):
        badoutput = {1:'Box is not in the game board, please try again', 2:'Box has already been filled, please try again'}

        #Here, the player makes his mark on the board, and the program detects if
        #there are any wrong inputs
        output = player.play(board.matrix,
                int(input(f'{player.pname}, choose a box to place a \'{player.mark}\' into \n')),
                board.turnnumber)

        if type(output) is int:
            badturn = True
            while badturn:
                output = player.play(board.matrix, input(badoutput[output]), board.turnnumber)
                if type(output) is list:
                    badturn = False

        #With a valid input, the program updates the turn number and checks for an endgame condition
        board.turnnumber = output[3]
        board.matrix = output[0]
        board.printboard()
        endgame = board.stopgame(output[1], output[2], player.pname)
        if endgame:
            return endgame
        else:
            return False

    #Setting up the game with board size and player names
    wrongentry = True
    size = int(input('Please enter the size of your board \n'))
    while wrongentry:

        if size >= 3:
            board = GameBoard(size)
            wrongentry = False

        if wrongentry:
            entry = input('Please enter an integer greater than or equal to 3')

    print(f'{board.length}x{board.length} board created')
    player1 = Player(input('Enter Player 1 name \n'), 'X', board.maxbox)
    player2 = Player(input('Enter Player 2 name \n'), 'O', board.maxbox)

    #Game starts
    board.printboard()
    while True:
        endgame = playerturn(player1, board)
        if endgame:
            print(endgame)
            break

        endgame = playerturn(player2, board)
        if endgame:
            print(endgame)
            break