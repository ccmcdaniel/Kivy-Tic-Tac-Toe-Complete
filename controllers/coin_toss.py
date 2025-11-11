from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
from kivy.app import App
from random import randint

class CoinTossScreen(Screen):
    player1_name  = StringProperty()
    btnHeads = ObjectProperty()
    btnTails = ObjectProperty()

    def on_click_confirm_selection(self):

        if self.btnHeads.state == 'down':
            self.toss_coin('heads')

        elif self.btnTails.state == 'down':
            self.toss_coin('tails')

    def toss_coin(self, face):
        app = App.get_running_app()

        toss_result = randint(0, 1)
        # heads - 0
        # tails - 1
        # Player 1 won
        if(face == 'heads' and toss_result == 0) or (face == 'tails' and toss_result == 1):
            self.manager.current = 'coin_toss_result'
            self.manager.current_screen.face_up_name = face
            self.manager.current_screen.winning_player_name = app.game_session.player1.name
            app.game_session.SetStartingPlayer(1)

        # Player 2 won
        else:
            self.manager.current_screen.face_up_name = face
            self.manager.current_screen.winning_player_name = app.game_session.player2.name
            app.game_session.SetStartingPlayer(2)

        
        