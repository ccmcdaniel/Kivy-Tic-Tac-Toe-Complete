import os
import kivy
from kivy.core.window import Window
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from widgets.widgets import *

# *************Controllers**********************
from controllers.main_menu import MainMenuScreen
from controllers.setup_players import SetupPlayersScreen
from controllers.coin_toss import CoinTossScreen
from controllers.coin_toss_result import *
from controllers.game_screen import *
from controllers.game_result import *

# ************Models****************************
from models.game_session import GameSession

window_scale = 1.0
default_window_size = (414, 896)
Window.size = default_window_size

Builder.load_file('tic_tac_toe_app.kv')

class ViewManager(ScreenManager):
    pass

class TicTacToeApp(App):
    def build(self):
        self.game_session = GameSession()
        self.view_manager = ViewManager()

        return self.view_manager
    
# used to load KV files from sub directories.
def load_kv_subdir(dir_name):
    screens_path = os.path.join(os.path.dirname(__file__), dir_name)
    for filename in os.listdir(screens_path):
        if filename.endswith('.kv'):
            Builder.load_file(os.path.join(screens_path, filename))

if __name__ == '__main__':
    # Loads all KV files in the "screens" folder
    load_kv_subdir('views')
    load_kv_subdir('widgets')

    app = TicTacToeApp()
    app.run()