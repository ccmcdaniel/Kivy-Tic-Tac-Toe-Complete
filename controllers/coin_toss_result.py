from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty

class CoinTossResultScreen(Screen):
    winning_player_name = StringProperty("")
    face_up_name = StringProperty("")

    def click_start_game(self):
        self.manager.current = 'game'
        self.manager.current_screen.setup_board()