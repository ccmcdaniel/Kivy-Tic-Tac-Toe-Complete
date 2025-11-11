class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

class Board:
    def __init__(self):
        # Initiate the Boardd
        self.ResetBoard()

    def ResetBoard(self):
        self.__grid = [] # store x or o

        for i in range(3):
            self.__grid.append([])
            for j in range(3):
                self.__grid[i].append('-')

    def SetTile(self, row, col, token):
        if(self.__grid[row][col] == '-'):
            self.__grid[row][col] = token
            return True
        else:   
            return False
        
    def CheckWinner(self):
        # x x x
        # - - -
        # - - -
        if ((self.__grid[0][0] == 'x') and (self.__grid[0][1] == 'x') and (self.__grid[0][2] == 'x')):
            return 'x'
        elif ((self.__grid[0][0] == 'o') and (self.__grid[0][1] == 'o') and (self.__grid[0][2] == 'o')):
            return 'o'
       
        # - - -
        # x x x
        # - - -
        elif ((self.__grid[1][0] == 'x') and (self.__grid[1][1] == 'x') and (self.__grid[1][2] == 'x')):
            return 'x'
        elif ((self.__grid[1][0] == 'o') and (self.__grid[1][1] == 'o') and (self.__grid[1][2] == 'o')):
            return 'o'

        # - - -
        # - - -
        # x x x
        elif ((self.__grid[2][0] == 'x') and (self.__grid[2][1] == 'x') and (self.__grid[2][2] == 'x')):
            return 'x'
        elif ((self.__grid[2][0] == 'o') and (self.__grid[2][1] == 'o') and (self.__grid[2][2] == 'o')):
            return 'o'

        # x - -
        # x - -
        # x - -
        elif ((self.__grid[0][0] == 'x') and (self.__grid[1][0] == 'x') and (self.__grid[2][0] == 'x')):
            return 'x'
        elif ((self.__grid[0][0] == 'o') and (self.__grid[1][0] == 'o') and (self.__grid[2][0] == 'o')):
            return 'o'

        # - x -
        # - x -
        # - x -
        elif ((self.__grid[0][1] == 'x') and (self.__grid[1][1] == 'x') and (self.__grid[2][1] == 'x')):
            return 'x'
        elif ((self.__grid[0][1] == 'o') and (self.__grid[1][1] == 'o') and (self.__grid[2][1] == 'o')):
            return 'o'

        # - - x
        # - - x
        # - - x
        elif ((self.__grid[0][2] == 'x') and (self.__grid[1][2] == 'x') and (self.__grid[2][2] == 'x')):
            return 'x'
        elif ((self.__grid[0][2] == 'o') and (self.__grid[1][2] == 'o') and (self.__grid[2][2] == 'o')):
            return 'o'
        
        # x - -
        # - x -
        # - - x
        elif ((self.__grid[0][0] == 'x') and (self.__grid[1][1] == 'x') and (self.__grid[2][2] == 'x')):
            return 'x'
        elif ((self.__grid[0][0] == 'o') and (self.__grid[1][1] == 'o') and (self.__grid[2][2] == 'o')):
            return 'o'

        # - - x
        # - x -
        # x - -
        elif ((self.__grid[0][2] == 'x') and (self.__grid[1][1] == 'x') and (self.__grid[2][0] == 'x')):
            return 'x'
        elif ((self.__grid[0][2] == 'o') and (self.__grid[1][1] == 'o') and (self.__grid[2][0] == 'o')):
            return 'o'
        
        else:
            return '-'

class GameSession:
    player1 = None
    player2 = None

    board = Board()

    def SetStartingPlayer(self, num):
        if(num == 1):
            self.active_player = self.player1
        elif(num == 2):
            self.active_player = self.player2

    def SwapPlayer(self):
        if(self.active_player == self.player1):
            self.active_player = self.player2
        else:
            self.active_player = self.player1




