from kivy.properties import ColorProperty
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.utils import get_color_from_hex as hex
from kivy.properties import StringProperty
from kivy.properties import NumericProperty
from kivy.properties import ColorProperty

class MainMenuButton(Button):
    bg_color_normal = ColorProperty(hex("#2D20E3"))
    bg_color_pressed = ColorProperty(hex("#A9A4F0"))

class CoinIcon(ToggleButton):
    bg_color_normal = ColorProperty(hex("#CCAA7D"))
    bg_color_pressed = ColorProperty(hex("#FFD7A3"))

class PlayerScoreHUD(BoxLayout):
    name = StringProperty("Player NA")
    score = StringProperty("XX")
    bg_color = ColorProperty(hex("#B24141"))
    text_color = ColorProperty(hex("#000000"))
    
    top_left = NumericProperty(0)
    top_right = NumericProperty(0)
    bottom_left = NumericProperty(0)
    bottom_right = NumericProperty(0)


class BoardTile(ToggleButton):
    pass

class GameBoard(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        for i in range(9):
            self.add_widget(BoardTile())
