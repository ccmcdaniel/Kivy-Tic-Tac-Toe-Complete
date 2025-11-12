from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty

class GameScreen(Screen):
    player1_name = StringProperty("Player 1")
    player1_score = StringProperty("0")
    
    player2_name = StringProperty("Player 2")
    player2_score = StringProperty("0")

    active_player_name = StringProperty()

    tile_0_0 = ObjectProperty()
    tile_0_1 = ObjectProperty()
    tile_0_2 = ObjectProperty()
    
    tile_1_0 = ObjectProperty()
    tile_1_1 = ObjectProperty()
    tile_1_2 = ObjectProperty()
    
    tile_2_0 = ObjectProperty()
    tile_2_1 = ObjectProperty()
    tile_2_2 = ObjectProperty()
    

    def setup_board(self):
        app = App.get_running_app()

        self.player1_name = app.game_session.player1.name
        self.player2_name = app.game_session.player2.name
        self.active_player_name = app.game_session.active_player.name


    def on_press_tile(self, tile_clicked):
        app = App.get_running_app()

        print(f"Clicked tile {tile_clicked.tile_row}, {tile_clicked.tile_col}")

        # if Player 1 is Active
        if(app.game_session.CheckActivePlayer(1)):
            tile_clicked.text = 'x'
        else:
            tile_clicked.text = 'o'
        
        app.game_session.MarkTile(tile_clicked.tile_row, tile_clicked.tile_col)

        # disable button upon being clicked
        tile_clicked.disabled = True

        # If a win state is reached on the active player, then 
        if(app.game_session.CheckWinner()):
            app.game_session.ConcludeGame()
            self.manager.current = "game_result"

        # If all tiles are disabled, game is over and a tie occurred
        elif(self.check_all_disabled()):
            self.manager.current = "game_result"
        
        # if game is still in session, then swap the player and continue
        else:    
            app.game_session.SwapPlayer()
            self.active_player_name = app.game_session.active_player.name
            


    # checks to see if all tiles are disabled.
    def check_all_disabled(self):
        tiles = (
            self.tile_0_0, self.tile_0_1, self.tile_0_2, 
            self.tile_1_0, self.tile_1_1, self.tile_1_2, 
            self.tile_2_0, self.tile_2_1, self.tile_2_2, 
        )

        for tile in tiles:
            if tile.disabled == False:
                return False
        
        return True




