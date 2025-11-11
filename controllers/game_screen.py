from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.properties import StringProperty

class GameScreen(Screen):
    player1_name = StringProperty("Player 1")
    player1_score = StringProperty("0")
    
    player2_name = StringProperty("Player 2")
    player2_score = StringProperty("0")

    active_player_name = StringProperty()

    def setup_board(self):
        app = App.get_running_app()

        self.player1_name = app.game_session.player1.name
        self.player2_name = app.game_session.player2.name
        self.active_player_name = app.game_session.active_player.name





