from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivy.app import App
from models.game_session import Player

class SetupPlayersScreen(Screen):
    player1_name = StringProperty()
    player2_name = StringProperty()


    def setup_screen(self):
        self.player1_name = ""
        self.player2_name = ""
    
    def set_players(self):
        app = App.get_running_app()
        app.game_session.player1 = Player(self.player1_name)
        app.game_session.player2 = Player(self.player2_name)
        
        self.manager.current = "coin_toss"
        self.manager.current_screen.player1_name = self.player1_name

