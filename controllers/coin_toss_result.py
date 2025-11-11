from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty

class CoinTossResultScreen(Screen):
    winning_player_name = StringProperty("")
    face_up_name = StringProperty("")