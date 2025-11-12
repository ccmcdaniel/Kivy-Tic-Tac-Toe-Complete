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
    active_player = None
    game_over = False

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

    def CheckActivePlayer(self, player_num):
        if(player_num == 1 and self.active_player == self.player1):
            return True
        
        elif(player_num == 2 and self.active_player == self.player2):
            return True
        
        else:
            return False
        
    def MarkTile(self, row, col):

        if(self.active_player == self.player1):
            token = 'x'
        else:
            token = 'o'
        
        self.board.SetTile(row, col, token)

    def CheckWinner(self):
        result = self.board.CheckWinner()

        # Player 1 Won
        if(result == 'x'):
            return True
        elif(result == 'o'):
            return True
        else:
            return False
        
    def GetWinnerName(self):
        result = self.board.CheckWinner()

        # Player 1 Won
        if(result == 'x'):
            return self.player1.name
        elif(result == 'o'):
            return self.player2.name
        else:
            return ""
        
    def ConcludeGame(self):
        if (self.game_over == True):
            return
        
        result = self.board.CheckWinner()

        # Player 1 Won
        if(result == 'x'):
            self.player1.score += 1
            self.game_over = True
        elif(result == 'o'):
            self.player2.score += 1
            self.game_over = True

    def StartNewGame(self):
        self.board.ResetBoard()
        self.game_over = False

        winner = self.CheckWinner()

        # determine the loser, which will go first on the new game.
        if(winner == 'x'):
            self.active_player = self.player2
        elif(winner == 'o'):
            self.active_player = self.player1
        else: # if tie, coin toss to select starting player
            import random
            coin_toss = random.randint(0, 1)
            if(coin_toss == 0):
                self.active_player = self.player1
            else:
                self.active_player = self.player2

        





